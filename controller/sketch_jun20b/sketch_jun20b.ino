//#include <SoftwareSerial.h>

//SoftwareSerial mySerial(8, 7); // RX, TX
//
//void setup() {
//  // Open serial communications and wait for port to open:
//  Serial.begin(9600);
//  while (!Serial) {
//    ; // wait for serial port to connect. Needed for native USB port only
//  }
//
//
//  Serial.println("Goodnight moon!");
//
//  // set the data rate for the SoftwareSerial port
//  mySerial.begin(115200);
//  mySerial.println("Hello, world?");
//}
//
//void loop() { // run over and over
//  if (mySerial.available()) {
//    Serial.write(mySerial.read());
//  }
//  if (Serial.available()) {
//    mySerial.write(Serial.read());
//  }
//}

#include <SoftwareSerial.h>
//
SoftwareSerial serial(8, 7); // RX, TX
int dingen = 0;

void setup() {
  // put your setup code here, to run once:
  serial.begin( 115200 );
  Serial.begin( 115200 );
}

void loop() {
  // put your main code here, to run repeatedly:
    serial.println("ping:");
    Serial.println(dingen);
    dingen++;
  
  delay(5000);
}
