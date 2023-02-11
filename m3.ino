#include <Wire.h>
#include <ESP8266WiFi.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin(4, 5);
  mpu.initialize();
  Serial.println("Put the MPU6050 flat and still");
  delay(5000); // wait for sensor to settle
}

void loop() {
  int16_t ax, ay, az, gx, gy, gz;
  int16_t ax_offset = 480;
  int16_t ay_offset = -214;
  int16_t az_offset = 16220;
  int16_t gx_offset = -726;
  int16_t gy_offset = 214;
  int16_t gz_offset = 178;

  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Apply offset values
  ax -= ax_offset;
  ay -= ay_offset;
  az -= az_offset;
  gx -= gx_offset;
  gy -= gy_offset;
  gz -= gz_offset;

  Serial.print("ax: "); Serial.print(ax);
  Serial.print(" ay: "); Serial.print(ay);
  Serial.print(" az: "); Serial.print(az);
  Serial.print(" gx: "); Serial.print(gx);
  Serial.print(" gy: "); Serial.print(gy);
  Serial.print(" gz: "); Serial.println(gz);
  
  delay(1000);
}
