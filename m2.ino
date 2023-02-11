#include <ESP8266WiFi.h>

const char *ssid = "NodeMCU";
const char *password = "password";

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("NodeMCU IP address: ");
  Serial.println(IP);
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New client connected");
    while (client.connected()) {
      String data = "Node MCU sends its wishes";
      client.println(data);
      delay(500);
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}