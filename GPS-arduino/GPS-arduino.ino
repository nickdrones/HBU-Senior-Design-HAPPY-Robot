#include <SparkFun_u-blox_GNSS_Arduino_Library.h> //http://librarymanager/All#SparkFun_u-blox_GNSS
#include <u-blox_config_keys.h>
#include <Wire.h> //Needed for I2C to GNSS

SFE_UBLOX_GNSS myGNSS;

long lastTime = 0; //Simple local timer. Limits amount if I2C traffic to u-blox module.

void setup()
{
  Serial.begin(115200);
  while (!Serial); //Wait for user to open terminal

  Wire.begin();

  if (myGNSS.begin() == false) //Connect to the u-blox module using Wire port
  {
    Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
    while (1);
  }

  myGNSS.setI2COutput(COM_TYPE_UBX); //Set the I2C port to output UBX only (turn off NMEA noise)
  //myGNSS.saveConfiguration(); //Optional: Save the current settings to flash and BBR
}

long last_long = 0;
long last_lat = 0;
long latitude = 0;
long longitude = 0;
String sdata = "";
int incomingByte = 0; // for incoming serial data

void loop()
{
  //Query module only every second. Doing it more often will just cause I2C traffic.
  //The module only responds when a new position is available
  incomingByte = Serial.read();
  // send data only when you receive data:
  if (incomingByte != 10) {
    if (incomingByte == 79) {Serial.println(longitude);}
    if (incomingByte == 65) {Serial.println(latitude);}
    if (incomingByte == 66) {Serial.println(String(longitude) + "," + String(latitude));}
  }
  if (millis() - lastTime > 1000)
  {
    lastTime = millis(); //Update the timer
    latitude = myGNSS.getLatitude();
    longitude = myGNSS.getLongitude();
  }
}
