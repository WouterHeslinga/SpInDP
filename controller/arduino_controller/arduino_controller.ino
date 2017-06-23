#include <stdint.h>
#include <SeeedTouchScreen.h>
#include <TFTv2.h>
#include <SPI.h>
#include <ArduinoJson.h>

// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include "I2Cdev.h"

#include "MPU6050_6Axis_MotionApps20.h"
//#include "MPU6050.h" // not necessary if using MotionApps include file

// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for SparkFun breakout and InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 mpu;
//MPU6050 mpu(0x69); // <-- use for AD0 high

#define OUTPUT_READABLE_YAWPITCHROLL

//#define LED_PIN 13 // (Arduino is 13, Teensy is 11, Teensy++ is 6)
//bool blinkState = false;

// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer

int switch_toggle = 0;
int switch_toggle_state = 0;


// ================================================================
// ===               INTERRUPT DETECTION ROUTINE                ===
// ================================================================

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
    mpuInterrupt = true;
}

void menu();
void scherm();
void touchscreentouch();
void touchscreenscherm();
void bluetooth();
void gyrosensor();

//SoftwareSerial serial(7, 8); // RX, TX
TouchScreen ts = TouchScreen(XP, YP, XM, YM);

//int schermkeuze = 0;      //variabele om te kijken of het menu op het scherm staat
//int keuze = 1;            //variabele voor de keuze die geselecteerd is
float voltage = 11.1;     //variabele voor informatie die op het scherm kan staan
float voltagelast = 0;
int Switch = 0;
int Switchlast = 0;
float xvalgyro = 0;
float xvalgyrolast = 0;
float yvalgyro = 0;
float yvalgyrolast = 0;
float zvalgyro = 0;
float zvalgyrolast = 0;

//Pins
int pinJoyX = A6;
int pinJoyY = A7;

struct Values {
  //Menu and display
  int screen_choice = 1;
  int show_screen = 0;
  //Joystick
  int joy_x = 0;
  int joy_y = 0;
  //Gyro
  int pitch = 0;
  int yaw = 0;
  int rol = 0;
  //Changed bools
  bool screen_changed = false;
  bool joy_changed = false;
  bool gyro_changed = false;
};
Values values;
Values last_values;
bool values_changed = false;

const int SW_pin = 3;

unsigned long lastTime = 0;
unsigned long lastHeartbeat = 0;

/**
* Sets up the pins and other hardware like the display and gyrosensor
*/
void setup() {
  //Serial.begin(115200);

  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
   
  //TFT_BL_ON;            //turn on the background light 
  Tft.TFTinit();          //init TFT library

  // join I2C bus (I2Cdev library doesn't do this automatically)
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

    // initialize serial communication
    // (115200 chosen because it is required for Teapot Demo output, but it's
    // really up to you depending on your project)
    Serial.begin(115200);
    while (!Serial); // wait for Leonardo enumeration, others continue immediately

    // NOTE: 8MHz or slower host processors, like the Teensy @ 3.3v or Ardunio
    // Pro Mini running at 3.3v, cannot handle this baud rate reliably due to
    // the baud timing being too misaligned with processor ticks. You must use
    // 38400 or slower in these cases, or use some kind of external separate
    // crystal solution for the UART timer.

    // initialize device
    Tft.drawString("Initializing I2C devices...",10,10,1,WHITE);
    mpu.initialize();

    // verify connection
    Tft.drawString("Testing device connections...",10,30,1,WHITE);
    if (mpu.testConnection()){
      Tft.drawString("MPU6050 connection successful",10,50,1,WHITE);
    }
    else {
      Tft.drawString("MPU6050 connection failed",10,50,1,WHITE);
    }

    delay(200);
    
    // load and configure the DMP
    Tft.drawString("Initializing DMP...",10,70,1,WHITE);
    devStatus = mpu.dmpInitialize();

    // supply your own gyro offsets here, scaled for min sensitivity
    mpu.setXGyroOffset(220);
    mpu.setYGyroOffset(76);
    mpu.setZGyroOffset(-85);
    mpu.setZAccelOffset(1788); // 1688 factory default for my test chip

    // make sure it worked (returns 0 if so)
    if (devStatus == 0) {
        // turn on the DMP, now that it's ready
        Tft.drawString("Enabling DMP...",10,90,1,WHITE);
        mpu.setDMPEnabled(true);

        // enable Arduino interrupt detection
        Tft.drawString("Enabling interrupt detection (Arduino external interrupt 0)...",10,110,1,WHITE);
        attachInterrupt(0, dmpDataReady, RISING);
        mpuIntStatus = mpu.getIntStatus();

        // set our DMP Ready flag so the main loop() function knows it's okay to use it
        Tft.drawString("DMP ready! Waiting for first interrupt...",10,130,1,WHITE);
        dmpReady = true;

        // get expected DMP packet size for later comparison
        packetSize = mpu.dmpGetFIFOPacketSize();
    } else {
        // ERROR!
        // 1 = initial memory load failed
        // 2 = DMP configuration updates failed
        // (if it's going to break, usually the code will be 1)
        Tft.drawString("DMP Initialization failed (code ",10,170,1,WHITE);
        //Tft.drawString(devStatus,10,190,2,WHITE);
        Tft.drawString(")",10,210,1,WHITE);
    }

    delay(200);

  
  scherm();               //hoofdscherm op het scherm zetten
}

/**
* Gets the input of the touchscreen and changes the value of the selected
* screen and if the menu needs to be displayed. Also handles the menu selection
* logic
*/
void input_touchscreen() {
    // a point object holds x y and z coordinates.
  Point p = ts.getPoint();      //kijken of en waar er op het scherm gedrukt wordt

  //map the ADC value read to into pixel co-ordinates
  p.x = map(p.x, TS_MINX, TS_MAXX, 0, 240);
  p.y = map(p.y, TS_MINY, TS_MAXY, 0, 320);

  // we have some minimum pressure we consider 'valid'
  // pressure of 0 means no pressing!
  if (p.z > __PRESURE) {        //om te bepalen of er op een knop wordt gedrukt
      //om te bepalen welke knop er wordt ingedrukt
      if(p.y > 7 && p.y < 27 && p.x > 7 && p.x < 62 && values.screen_choice == 0)
      {
        menu();           //menu op het scherm zetten
        values.show_screen = 1;
      }
      else if (p.y > 7 && p.y < 27 && p.x > 7 && p.x < 62 && values.screen_choice == 1)
      {
        scherm();
        values.show_screen = 0;
      }
      else if (p.y > 7 && p.y < 30 && p.x > 70 && p.x < 220 && values.screen_choice == 1)
      {
        scherm();
        values.show_screen = 0;
        values.screen_choice = 1;
      }
      else if (p.y > 31 && p.y < 57 && p.x > 70 && p.x < 220 && values.screen_choice == 1)
      {
        scherm();
        values.show_screen = 0;
        values.screen_choice = 2;
      }
      else if (p.y > 58 && p.y < 84 && p.x > 70 && p.x < 220 && values.screen_choice == 1)
      {
        scherm();
        values.show_screen = 0;
        values.screen_choice = 3;
      }
      else if (p.y > 85 && p.y < 111 && p.x > 70 && p.x < 220 && values.screen_choice == 1)
      {
        scherm();
        values.show_screen = 0;
        values.screen_choice = 4;
      }
      else if (p.y > 112 && p.y < 138 && p.x > 70 && p.x < 220 && values.screen_choice == 1)
      {
        scherm();
        values.show_screen = 0;
        values.screen_choice = 5;
      }

      voltagelast = 0;
      Switchlast = 0;
  }
}

/**
* Gets the input from the gyro and converts it automatically
* to degrees, result is a pitch yaw and roll
*/
void input_gyro() {
  Quaternion q;
  VectorFloat gravity;
  float ypr[3];

  // if programming failed, don't try to do anything
  if (!dmpReady) return;
  // wait for MPU interrupt or extra packet(s) available
  while (!mpuInterrupt && fifoCount < packetSize ) { }

  // reset interrupt flag and get INT_STATUS byte
  mpuInterrupt = false;
  mpuIntStatus = mpu.getIntStatus();

  //Serial.println(F("get FIFO count!"));
  // get current FIFO count
  fifoCount = mpu.getFIFOCount();

  //Serial.println(F("check for overflow!"));
  // check for overflow (this should never happen unless our code is too inefficient)
  if ((mpuIntStatus & 0x10) || fifoCount == 1024) {
      // reset so we can continue cleanly
      mpu.resetFIFO();
      //Serial.println(F("FIFO overflow!"));

  // otherwise, check for DMP data ready interrupt (this should happen frequently)
  } 
  else if (mpuIntStatus & 0x02) {
      // wait for correct available data length, should be a VERY short wait
      while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();

      // read a packet from FIFO
      mpu.getFIFOBytes(fifoBuffer, packetSize);
      mpu.resetFIFO();
      
      // track FIFO count here in case there is > 1 packet available
      // (this lets us immediately read more without waiting for an interrupt)
      fifoCount -= packetSize;

      #ifdef OUTPUT_READABLE_YAWPITCHROLL
          // display Euler angles in degrees
          mpu.dmpGetQuaternion(&q, fifoBuffer);
          mpu.dmpGetGravity(&gravity, &q);
          mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
          values.pitch = (ypr[1] * 180/M_PI);    //lees joystick waarden
          values.rol = (ypr[2] * 180/M_PI);
          values.yaw = (ypr[0] * 180/M_PI);
      #endif
  }
}

/**
* Checks if the values are changed so that the screen render knows what te re render
*/
void check_values_changed() {
  values.screen_changed = (values.screen_choice != last_values.screen_choice ||
    values.show_screen != last_values.show_screen);
  values.joy_changed = (values.joy_x != last_values.joy_x ||
    values.joy_y != last_values.joy_x);
  values.gyro_changed = (values.pitch != last_values.pitch ||
    values.yaw != last_values.yaw ||
    values.rol != last_values.rol);
}

/**
* Updates all the inputs and then checks for changes
*/
void input() {
  last_values = values;
  //Touchscreen
  input_touchscreen();

  //Joysticks
  values.joy_x = analogRead(pinJoyX);
  values.joy_y = analogRead(pinJoyY);  

  //Gyro
  input_gyro();

  check_values_changed();
}

/**
* Runs every cycle
*/
void loop() {
  input();
  unsigned long now = millis();
  int timeChange = (now - lastTime);  // Bereken hoeveel tijd er voorbij is gegaan
  int heartbeatTimeout = (now - lastHeartbeat);
  //Elke seconde een heartbeat sturen om 
  if(timeChange>=50) {
    touchscreenscherm();
    joyInput();
    lastTime = now;
  }
  if(heartbeatTimeout >= 2500) {
    Serial.print("ping\n");
    lastHeartbeat = now;
  }

  //bluetooth();

}

String old_state = "idle";
void joyInput() {
  String state = old_state;
  if(values.joy_x > 700) {
    //Serial.print("up");
    state = "0";
  } else if (values.joy_x < 400) {
    //Serial.print("down");
    state = "180";
  } else if (values.joy_y > 700) {
    //Serial.print("left");
    state = "270";
  } else if (values.joy_y < 400) {
    //Serial.print("right");
    state = "90";
  } else {
    state = "idle";
  }

  if(state != old_state) {
    old_state = state;
    Serial.print((String)"motion_state:" + state + "\n");
    
  }
}

void touchscreenscherm() {
  int xval = 0;
  int yval = 0;
  if(values.show_screen != 1) {
    switch(values.screen_choice) {
      case 1:
        Tft.drawString("Manueel",73,10,2,WHITE);
        Tft.drawString("Joystick",10,180,2,WHITE);
        Tft.drawString("X =",10,200,2,WHITE);
        Tft.drawString("Y =",130,200,2,WHITE);  // draw string: "Voltage", (10, 200), size: 2, color: WHITE
        Tft.drawString("Switch =",10,220,2,WHITE);
        Tft.drawString("Gyrosensor",10,100,2,WHITE);
        Tft.drawString("X =",10,120,2,WHITE);
        Tft.drawString("Y =",125,120,2,WHITE);
        Tft.drawString("Z =",10,140,2,WHITE);

        Switch = digitalRead(SW_pin);
        if (values.show_screen != 1 && values.joy_changed)  //kijken of er waarden zijn verandert
        {
          Tft.fillRectangle(50, 200, 75,15,BLACK);
          Tft.drawNumber(values.joy_x,50,200,2,WHITE);
          Tft.fillRectangle(170, 200, 75,15,BLACK);
          Tft.drawNumber(values.joy_y,170,200,2,WHITE);
          Tft.fillRectangle(110, 220, 15,15,BLACK);
          Tft.drawNumber(Switch,110,220,2,WHITE);
          Switchlast = Switch;
        }
        
        
        xvalgyro = values.yaw;
        yvalgyro = values.pitch;
        zvalgyro = values.rol;
        if ((xvalgyro != xvalgyrolast || yvalgyro != yvalgyrolast || zvalgyro != zvalgyrolast) && values.show_screen != 1)  //kijken of er waarden zijn verandert
        {
          Tft.fillRectangle(50, 120, 75,15,BLACK);
          Tft.drawFloat(xvalgyro,2,50,120,2,WHITE);
          Tft.fillRectangle(165, 120, 75,15,BLACK);
          Tft.drawFloat(yvalgyro,2,165,120,2,WHITE);
          Tft.fillRectangle(50, 140, 85,15,BLACK);
          Tft.drawFloat(zvalgyro,2,50,140,2,WHITE);
        }
        break;
      case 2:
        Tft.drawString("Keuze 2",73,10,2,WHITE);
        break;
      case 3:
        Tft.drawString("Keuze 3",73,10,2,WHITE);
        break;
      case 4:
        Tft.drawString("Keuze 4",73,10,2,WHITE);

        xval = values.pitch;
        yval = values.rol;
        xval = map(xval, -40, 40, 0, 230);
        yval = map(yval, -30, 30, 0, 310);
        xval = constrain(xval, 0, 230);
        yval = constrain(yval, 0, 310);
        Tft.fillRectangle(xval, yval, 10,10,random(0xFFFF));

        if(digitalRead(SW_pin) == 0){
          scherm();
        }
        
        break;
      case 5:
        Tft.drawString("Keuze 5",73,10,2,WHITE);
        xval = values.joy_x;
        yval = values.joy_y;
        xval = map(xval, 0, 1023, 0, 230);
        yval = map(yval, 0, 1023, 0, 310);
        xval = constrain(xval, 0, 230);
        yval = constrain(yval, 0, 310);
        Tft.fillRectangle(xval, yval, 10,10,random(0xFFFF));

        if(digitalRead(SW_pin) == 0){
          scherm();
        }
        
        break;
    }
  }
    

    if (voltage != voltagelast && values.show_screen != 1)  //kijken of er waarden zijn verandert
    {
      Tft.fillRectangle(120, 160, 50,15,BLACK);
      Tft.drawFloat(voltage,1,120,160,2,WHITE);   // draw float: voltage, (120, 200), size: 2, decimal: 1, color: WHITE
      voltagelast = voltage;
    }

    //Serial.println(F("Touchscreen scherm!!!"));
    
}

void menu() {   //functie om het menu op het scherm te zetten
  Tft.fillRectangle(70, 7, 150, 250, WHITE);
  Tft.drawString("Manueel",73,10,2,BLACK);
  Tft.drawString("Keuze 2",73,37,2,BLACK);
  Tft.drawString("Keuze 3",73,64,2,BLACK);
  Tft.drawString("Keuze 4",73,91,2,BLACK);
  Tft.drawString("Keuze 5",73,118,2,BLACK);
}

void scherm() {   //functie om het standaard scherm op het scherm te zetten
  
  //Tft.fillRectangle(70, 7, 150, 250, BLACK);  //de rechthoek van het menu zwart maken
  Tft.fillScreen(0, 240, 0, 320, BLACK);
  Tft.drawRectangle(8, 7, 54,20,WHITE);
  Tft.drawString("MENU",10,10,2,WHITE);       // draw string: "MENU", (10, 10), size: 2, color: WHITE
  Tft.drawString("IDP Groep 6 Robert",10,310,1,random(0xFFFF));
  Tft.drawString("Voltage:",10,160,2,WHITE);  // draw string: "Voltage", (10, 200), size: 2, color: WHITE
  
}