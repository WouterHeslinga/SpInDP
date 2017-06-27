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

// ================================================================
// ===               INTERRUPT DETECTION ROUTINE                ===
// ================================================================

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
    mpuInterrupt = true;
}

//Function declerations
void menu();
void init_screen();
void render();
void gyrosensor();
void handle_joystick();
bool in_rekt(int px, int py, int x, int y, int w, int h);

TouchScreen ts = TouchScreen(XP, YP, XM, YM);

float voltage = 11.1;     //variabele voor informatie die op het scherm kan staan
float voltagelast = 0;

//Pins
int pinJoyX = A6;
int pinJoyY = A7;

enum States {
  MANUAL,
  BALLOON,
  FURY_ROAD,
  EGG_GAME,
  DANCE
};

enum Symbols {
  NONE,
  SPADE,
  CLUB,
  DIAMOND,
  HEART
};

struct Values {
  //Menu and display
  int screen_choice = 1;
  int show_menu = 0;
  //Joystick
  int joy_x = 0;
  int joy_y = 0;
  bool joy_press = false;
  //Gyro
  int pitch = 0;
  int yaw = 0;
  int roll = 0;
  //State
  States state = MANUAL;
  //Changed bools
  bool screen_changed = false;
  bool joy_changed = false;
  bool gyro_changed = false;
  bool switch_changed = false;
  bool state_changed = false;
};

Values values;
Values last_values;
bool values_changed = false;

//Stuff for the egg selection
bool show_egg_select = false;
Symbols selected_symbol = NONE;
Symbols selected_symbol_second = NONE;

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
  init_screen();
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
    if(show_egg_select) {
      Symbols symbol = NONE;
      if(in_rekt(p.x, p.y, 5, 75, 110, 55)) { // Club
        symbol = CLUB;
      } else if (in_rekt(p.x, p.y, 125, 75, 110, 55)) { // Spade
        symbol = SPADE;
      } else if (in_rekt(p.x, p.y, 5, 145, 110, 55)) { // Diamond
        symbol = DIAMOND;
      } else if (p.x, p.y, 125, 145, 110, 55) { // Heart
        symbol = HEART;
      }

      if (symbol != NONE) {
        if (selected_symbol == NONE) {
          selected_symbol = symbol;
          render_egg_menu();
        } else {
          if (selected_symbol == symbol) {
            selected_symbol = NONE;
            render_egg_menu();
          } else {
            Serial.print((String)"egg:" + selected_symbol + ":" + symbol + "\n");
            selected_symbol_second = symbol;
            show_egg_select = false;
            init_screen();
          }
        }
      }
    }
    //om te bepalen welke knop er wordt ingedrukt
    if(p.y > 7 && p.y < 27 && p.x > 7 && p.x < 62 && values.show_menu == 0)
    {
      menu();           //menu op het scherm zetten
      values.show_menu = 1;
    }
    else if (p.y > 7 && p.y < 27 && p.x > 7 && p.x < 62 && values.show_menu == 1)
    {
      init_screen();
      values.show_menu = 0;
    }
    else if (p.y > 7 && p.y < 30 && p.x > 70 && p.x < 220 && values.show_menu == 1)
    {
      init_screen();
      values.show_menu = 0;
      values.state = MANUAL;
    }
    else if (p.y > 31 && p.y < 57 && p.x > 70 && p.x < 220 && values.show_menu == 1)
    {
      values.show_menu = 0;
      values.state = BALLOON;
      Serial.print((String)"state:balloon\n");
      init_screen();
    }
    else if (p.y > 58 && p.y < 84 && p.x > 70 && p.x < 220 && values.show_menu == 1)
    {
      values.show_menu = 0;
      values.state = FURY_ROAD;
      Serial.print((String)"state:fury_road\n");      
      init_screen();
    }
    else if (p.y > 85 && p.y < 111 && p.x > 70 && p.x < 220 && values.show_menu == 1)
    {
      values.show_menu = 0;
      init_screen();
      values.state = EGG_GAME;
      selected_symbol = NONE;
      selected_symbol_second = NONE;
      show_egg_select = true;
      render_egg_menu();
    }
    else if (p.y > 112 && p.y < 138 && p.x > 70 && p.x < 220 && values.show_menu == 1)
    {
      values.state = DANCE;
      values.show_menu = 0;
      Serial.print((String)"state:dance\n");      
      init_screen();
    }
    if (values.state != EGG_GAME)
      show_egg_select = false;
  }
}

bool in_rekt(int px, int py, int x, int y, int w, int h) {
  int x2 = x + w;
  int y2 = y + h;
  return
    px >= x && px <= x2 &&
    py >= y && py <= y2;
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
          values.roll = (ypr[2] * 180/M_PI);
          values.yaw = (ypr[0] * 180/M_PI);
      #endif
  }
}

/**
* Checks if the values are changed so that the screen render knows what te re render
*/
void check_values_changed() {
  values.screen_changed = (values.screen_choice != last_values.screen_choice ||
    values.show_menu != last_values.show_menu);
  values.joy_changed = (values.joy_x != last_values.joy_x ||
    values.joy_y != last_values.joy_x);
  values.gyro_changed = (values.pitch != last_values.pitch ||
    values.yaw != last_values.yaw ||
    values.roll != last_values.roll);
  values.switch_changed = values.joy_press != last_values.joy_press;
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
  values.joy_press = digitalRead(SW_pin) != 1;

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
  int timeChange = (now - lastTime);
  int heartbeatTimeout = (now - lastHeartbeat);
  if(timeChange>=50) {
    render();
    handle_joystick();
    lastTime = now;
  }
  if(heartbeatTimeout >= 2500) { //Send ping every 2.5 seconds to keep the bluetooth alive (born to be alive!)
    Serial.print("ping\n");
    lastHeartbeat = now;
  }

}

String old_state = "idle";
void handle_joystick() {
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

  if(values.switch_changed) {
    Serial.print((String)"joyclick\n");
  }
}

void render() {
  int xval = 0;
  int yval = 0;

  if(!show_egg_select) {
    if(values.show_menu != 1) {
      switch(values.state) {
        case MANUAL: Tft.drawString("Manual",73,10,2,WHITE); break;
        case BALLOON: Tft.drawString("Balloon",73,10,2,WHITE); break;
        case FURY_ROAD: Tft.drawString("Fury Road",73,10,2,WHITE); break;
        case EGG_GAME: Tft.drawString("Egg Game",73,10,2,WHITE); break;
        case DANCE: Tft.drawString("Dance",73,10,2,WHITE); break;
      }

      Tft.drawString("Gyrosensor",10,100,2,WHITE);
      Tft.drawString("X =",10,120,2,WHITE);
      Tft.drawString("Y =",125,120,2,WHITE);
      Tft.drawString("Z =",10,140,2,WHITE);
      Tft.drawString("Joystick",10,180,2,WHITE);
      Tft.drawString("X =",10,200,2,WHITE);
      Tft.drawString("Y =",130,200,2,WHITE);
      Tft.drawString("Switch =",10,220,2,WHITE);
      Tft.drawString("Symbol =",10, 260,2,WHITE);
      Tft.drawString("Symbol2=",10, 280,2,WHITE);

      Tft.fillRectangle(160,260,70,15, BLACK);
      switch (selected_symbol) {
        case NONE: Tft.drawString("None", 160, 260,2,WHITE); break;
        case SPADE: Tft.drawString("Spade", 160, 260,2,WHITE); break;
        case CLUB: Tft.drawString("Club", 160, 260,2,WHITE); break;
        case DIAMOND: Tft.drawString("Diamond", 160, 260,2,WHITE); break;
        case HEART: Tft.drawString("Heart", 160, 260,2,WHITE); break;
      }

      Tft.fillRectangle(160,280,70,15, BLACK);
      switch (selected_symbol_second) {
        case NONE: Tft.drawString("None", 160, 280,2,WHITE); break;
        case SPADE: Tft.drawString("Spade", 160, 280,2,WHITE); break;
        case CLUB: Tft.drawString("Club", 160, 280,2,WHITE); break;
        case DIAMOND: Tft.drawString("Diamond", 160, 280,2,WHITE); break;
        case HEART: Tft.drawString("Heart", 160, 280,2,WHITE); break;
      }

      if (values.joy_changed) {
        Tft.fillRectangle(50, 200, 75,15,BLACK);
        Tft.drawNumber(values.joy_x,50,200,2,WHITE);
        Tft.fillRectangle(170, 200, 75,15,BLACK);
        Tft.drawNumber(values.joy_y,170,200,2,WHITE);
        Tft.fillRectangle(110, 220, 15,15,BLACK);
        Tft.drawNumber(values.joy_press,110,220,2,WHITE);
      }
      
      if (values.gyro_changed) {
        Tft.fillRectangle(50, 120, 75,15,BLACK);
        Tft.drawFloat(values.yaw,2,50,120,2,WHITE);
        Tft.fillRectangle(165, 120, 75,15,BLACK);
        Tft.drawFloat(values.pitch,2,165,120,2,WHITE);
        Tft.fillRectangle(50, 140, 85,15,BLACK);
        Tft.drawFloat(values.roll,2,50,140,2,WHITE);
      }
    }
      
    // if (voltage != voltagelast && values.show_menu != 1)  //kijken of er waarden zijn verandert
    // {
    //   Tft.fillRectangle(120, 160, 50,15,BLACK);
    //   Tft.drawFloat(voltage,1,120,160,2,WHITE);   // draw float: voltage, (120, 200), size: 2, decimal: 1, color: WHITE
    //   voltagelast = voltage;
    // }
  }
}

void render_egg_menu() {
    //Color egg
    Tft.drawString("Symbol:", 5, 50, 2, WHITE);

    Tft.fillRectangle(5, 75, 110, 55, selected_symbol == CLUB ? 0xFF00FF : 0x00FF00);
    Tft.fillRectangle(125, 75, 110, 55, selected_symbol == SPADE ? 0xFF00FF : 0x00FF00);
    Tft.fillRectangle(5, 145, 110, 55, selected_symbol == DIAMOND ? 0xFF00FF : 0x00FF00); 
    Tft.fillRectangle(125, 145, 110, 55, selected_symbol == HEART ? 0xFF00FF : 0x00FF00);

    Tft.drawString("Club", 20, 95, 2, BLACK);
    Tft.drawString("Spade", 135, 95, 2, BLACK);
    Tft.drawString("Diamond", 20, 160, 2, BLACK);
    Tft.drawString("Heart", 135, 160, 2, BLACK);
}

void menu() { //functie om het menu op het scherm te zetten
  Tft.fillRectangle(70, 7, 150, 250, WHITE);
  Tft.drawString("Manual",73,10,2,BLACK);
  Tft.drawString("Balloon",73,37,2,BLACK);
  Tft.drawString("Fury Road",73,64,2,BLACK);
  Tft.drawString("Egg Game",73,91,2,BLACK);
  Tft.drawString("Dance",73,118,2,BLACK);
}

void clear_screen() {
  Tft.fillScreen(0, 240, 0, 320, BLACK);
}

void init_screen() {   //functie om het standaard scherm op het scherm te zetten
  clear_screen();
  Tft.drawRectangle(8, 7, 54,35,WHITE);
  Tft.drawString("MENU",10,10,2,WHITE);
  Tft.drawString("IDP Groep 6 Robert",10,310,1,WHITE);
}