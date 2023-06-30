#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SoftwareSerial.h>

#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 4
#define CLK_PIN 13
#define DATA_PIN 11
#define CS_PIN 10

MD_Parola disp = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);
SoftwareSerial bluetooth(2, 3);

String receivedText = "";

void setup() {
  bluetooth.begin(9600);

  disp.begin();
  disp.setIntensity(1);
  disp.displayClear();

  Serial.begin(9600);
}

void loop() {
  if (bluetooth.available()) {
    char receivedChar = bluetooth.read();
    Serial.print("*");
    if (receivedChar != '\n') {
      receivedText += receivedChar;
    } else {
      Serial.println(receivedText);
      receivedText.trim();
      receivedText+=" ";
    }
  }
  scrollText();
}

void scrollText() {
  if (disp.displayAnimate()) {
    const char* textPtr = receivedText.c_str();
    disp.displayScroll(textPtr, PA_CENTER, PA_SCROLL_LEFT, 20);
    disp.displayReset();
    receivedText = "";
  }
}
