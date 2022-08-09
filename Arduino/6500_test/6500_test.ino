/***************************************************************************
* Example sketch for the MPU6500_WE library
*
* This sketch shows how to get acceleration, gyroscocope and temperature 
* data from the MPU6500. In essence, the difference to the MPU9250 is the
* missing magnetometer. The shall only show how to "translate" all other 
* MPU9250 example sketches for use of the MPU6500
* 
* For further information visit my blog:
*
* https://wolles-elektronikkiste.de/mpu9250-9-achsen-sensormodul-teil-1  (German)
* https://wolles-elektronikkiste.de/en/mpu9250-9-axis-sensor-module-part-1  (English)
* 
***************************************************************************/

#include <MPU6500_WE.h>
#include <Wire.h>
#define MPU6500_ADDR 0x68




/* There are several ways to create your MPU6500 object:
 * MPU6500_WE myMPU6500 = MPU6500_WE()              -> uses Wire / I2C Address = 0x68
 * MPU6500_WE myMPU6500 = MPU6500_WE(MPU6500_ADDR)  -> uses Wire / MPU6500_ADDR
 * MPU6500_WE myMPU6500 = MPU6500_WE(&wire2)        -> uses the TwoWire object wire2 / MPU6500_ADDR
 * MPU6500_WE myMPU6500 = MPU6500_WE(&wire2, MPU6500_ADDR) -> all together
 * Successfully tested with two I2C busses on an ESP32
 */
MPU6500_WE myMPU6500 = MPU6500_WE(MPU6500_ADDR);

void setup() {
  Serial.begin(115200);
  Wire.begin();
  if(!myMPU6500.init()){
//    Serial.println("MPU6500 does not respond");
  }
  else{
//    Serial.println("MPU6500 is connected");
  }
  
  /* The slope of the curve of acceleration vs measured values fits quite well to the theoretical 
   * values, e.g. 16384 units/g in the +/- 2g range. But the starting point, if you position the 
   * MPU6500 flat, is not necessarily 0g/0g/1g for x/y/z. The autoOffset function measures offset 
   * values. It assumes your MPU6500 is positioned flat with its x,y-plane. The more you deviate 
   * from this, the less accurate will be your results.
   * The function also measures the offset of the gyroscope data. The gyroscope offset does not   
   * depend on the positioning.
   * This function needs to be called at the beginning since it can overwrite your settings!
   */
//  Serial.println("Position you MPU6500 flat and don't move it - calibrating...");
  delay(100);
  myMPU6500.autoOffsets();
//  Serial.println("Done!");



  myMPU6500.setSampleRateDivider(1);
  myMPU6500.setAccRange(MPU6500_ACC_RANGE_8G);
  myMPU6500.setGyrRange(MPU6500_GYRO_RANGE_250);
  myMPU6500.enableAccDLPF(false);
  myMPU6500.disableGyrDLPF(MPU6500_BW_WO_DLPF_8800);

  //myMPU6500.enableAccAxes(MPU6500_ENABLE_XYZ);
//myMPU6500.enableGyrAxes(MPU6500_ENABLE_000);



//Wire.setClock(400000);
  
  delay(200);
}

void loop() {


//  double t1 = millis();
//  for (int i = 0; i < 1000; i++){
//  xyzFloat gValue = myMPU6500.getGValues();
//  //xyzFloat gyr = myMPU6500.getGyrValues();
//
//  }
//  double t2 = millis();
//
//  Serial.println(1 / ((t2 - t1) / 1000 / 1000));



//xyzFloat gValue = myMPU6500.getGValues();
//  Serial.print("X :");
//  Serial.print(gValue.x);
//  Serial.print(",");
//  Serial.print("Y :");
//  Serial.print(gValue.y);
//  Serial.print(",");
//  Serial.print("Z :");
//  Serial.println(gValue.z);


  long t1 = micros();
  xyzFloat G = myMPU6500.getGValues();
  xyzFloat gyr = myMPU6500.getGyrValues();
  Serial.print(millis());
   Serial.print(",");
  Serial.print(G.x, 6);
  Serial.print(",");
  Serial.print(G.y, 6);
  Serial.print(",");
  Serial.print(G.z, 6);
  Serial.print(",");
  Serial.print(gyr.x, 6);
  Serial.print(",");
  Serial.print(gyr.y, 6);
  Serial.print(",");
  Serial.print(gyr.z, 6);
  Serial.write(10);

  long t2 = micros();
  delay(50 - ((t2 - t1) / 1000));
M

//  Serial.print(gyr.x);
//  Serial.print(gyr.y);
//  Serial.println(gyr.z);

//  delay(100);
}
