#include <Wire.h> //Needed for I2C to GNSS

#include <SparkFun_u-blox_GNSS_Arduino_Library.h> //http://librarymanager/All#SparkFun_u-blox_GNSS
SFE_UBLOX_GNSS myGNSS;

long lastTime = 0; //Simple local timer. Limits amount if I2C traffic to u-blox module.

void setup()
{
  Serial.begin(115200);
  while (!Serial); //Wait for user to open terminal
  Serial.println("SparkFun u-blox Example");

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
void loop()
{


  //Query module only every second. Doing it more often will just cause I2C traffic.
  //The module only responds when a new position is available
  if (millis() - lastTime > 1000)
  {
    lastTime = millis(); //Update the timer

    latitude = myGNSS.getLatitude();
    //Serial.print(F("Lat: "));
    Serial.print(latitude);

    longitude = myGNSS.getLongitude();
    //Serial.print(F(" Long: "));
    //Serial.print(longitude);
    //Serial.print(F(" (degrees * 10^-7)"));
    Serial.println();

    //Serial.print(F("Difference in long: "));
    //Serial.print(last_long - longitude);
    //last_long = longitude;
    //Serial.print(F("  Difference in lat: "));
    //Serial.print(last_lat - latitude);
    //last_lat = latitude;
    //Serial.println();
    //Serial.println();

  }
}