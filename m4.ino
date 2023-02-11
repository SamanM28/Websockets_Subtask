#include <Wire.h>
#include <ESP8266WiFi.h>
#include <MPU6050.h>

const char *ssid = "NodeMCU";
const char *password = "password";

WiFiServer server(80);

MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("NodeMCU IP address: ");
  Serial.println(IP);

  server.begin();

  Wire.begin(4, 5);
  mpu.initialize();
  Serial.println("Put the MPU6050 flat and still");
  delay(5000); // wait for sensor to settle
}

void loop() {
  // WiFi Server
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New client connected");
    while (client.connected()) {
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

      String data = "ax: " + String(ax) +
                    " ay: " + String(ay) +
                    " az: " + String(az) +
                    " gx: " + String(gx) +
                    " gy: " + String(gy) +
                    " gz: " + String(gz);
      client.println(data);
      Serial.println(data);
      delay(500);
    }
    client.stop();
    Serial.println("Client disconnected");
  }

  delay(1000);
}
