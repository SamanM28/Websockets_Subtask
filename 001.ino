#include <SPI.h>
const int SSpin = 15;

void setup() {

pinMode(SSpin, OUTPUT);
SPI.begin();

}

void loop(){

for (int i = 0; i < 5; i++) {  //for each row

for (int j = 0; j < 5; j++) { //for each column

byte rows = B11111111;                //initialize rows inactive
byte columns = B00000000;   //initialize columns inative

bitWrite(rows, i, 0);           //write current row
bitWrite(columns, j, 1);     //write current column

digitalWrite(SSpin, HIGH);   //Disable any internal transference in the SN74HC595
SPI.transfer(columns);         //Transfer data to the SN74HC595
SPI.transfer(rows);               //Transfer data to the SN74HC595
digitalWrite(SSpin, LOW);  //Start the internal data transference in the SN74HC595
delay(3000);

}

}

}