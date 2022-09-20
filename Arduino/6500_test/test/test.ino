/*  PIE Mini Project 1: Bike Light
 *  Rowan Jansens, Olivia Chang
 *  9/15/22
*/

/* LIBRARIES */
#include <MPU9250_WE.h>
#include <Wire.h>

/* DEFINITIONS */
#define MPU9250_ADDR 0x68
MPU9250_WE myMPU9250 = MPU9250_WE(MPU9250_ADDR);
int NUM_LEDS = 5;
int leds[] = {3, 5, 6, 9, 10}; // data pins corresponding to LEDs
int buttonPin = 21; // data pin corresponding to button
long lastInterruptTime = 0; // define last interrupt time for debouncing

int mode = 0; // track bike light mode (see loop)
int NUM_MODES = 7;
bool led_switch = true;

void setup() {
  // Set up serial
  Serial.begin(9600);
  Serial.println("Sketch starting...");
  // Set up button pin
  pinMode(buttonPin, INPUT);
  // Attach interrupt function that is called when button pin state goes from LOW to HIGH
  attachInterrupt(digitalPinToInterrupt(buttonPin), incrementMode, RISING);
  // Set up LED pins
  for (int i = 0; i <= NUM_LEDS; i++) {
  pinMode(leds[i], OUTPUT);
  }

  // Set up accelerometer
  Wire.begin();
  if(!myMPU9250.init()){
  Serial.println("MPU9250 does not respond");
  }
  else{
  Serial.println("MPU9250 is connected");
  }
 
  myMPU9250.autoOffsets();
  myMPU9250.setSampleRateDivider(5);
  myMPU9250.setAccRange(MPU9250_ACC_RANGE_2G);
  myMPU9250.enableAccDLPF(true);
  myMPU9250.setAccDLPF(MPU9250_DLPF_6);  
}

// interrupt function
void incrementMode() {
  // get time of current interrupt
  long interruptTime = millis();

  if (interruptTime - lastInterruptTime >  200) {
    mode = (mode + 1) % NUM_MODES;
    Serial.println(mode);
  }

  lastInterruptTime = interruptTime;
}

void allOff() {
  for (int i = 0; i <= NUM_LEDS; i++) {
  digitalWrite(leds[i], LOW);
  }
}

void allOn() {
  for (int i = 0; i <= NUM_LEDS; i++) {
  digitalWrite(leds[i], HIGH);
  }
}

void scanner(unsigned long current_time){
  int scan_speed = 20;
 
  //loop through 16 states
  int led = (current_time / scan_speed) % 16;

  //reverse direction at end and define tail led
  int tail = led - 1;
  if (led >= 8){
  led =  16 - led;
  tail = led + 1;
  }

  //update leds
  for (int i = 2; i<7; i++){
  if (i == led){
    analogWrite(leds[i-2], 255);
  }
  else if (i == tail){
    analogWrite(leds[i-2], 128);
  }
  else{
    analogWrite(leds[i-2], 0);
  }
  }
}

void alternate(int second) {
  for (int i = 0; i <= NUM_LEDS; i++) {
  int currentValue;
  if (second % 2 == 0) {
    if (i % 2 == 0) {
      currentValue = LOW;
    } else {
      currentValue = HIGH;
    }
  } else {
    if (i % 2 == 0) {
      currentValue = HIGH;
    } else {
      currentValue = LOW;
    }
  }
  digitalWrite(leds[i], currentValue);
  }
}

void blinkLeds(int second) {
  for (int i = 0; i <= NUM_LEDS; i++) {
  if (second % 2 == 0) {
    digitalWrite(leds[i], HIGH);
  } else {
    digitalWrite(leds[i], LOW);
  }
  }
}

void tilt(xyzFloat angles){
  int led = -1 * (int(angles.y));
  if (led > 25){
  led = 25;
  } else if (led < -25){
  led = -25;
  }
 
  led = (led / 10) + 2;

  for (int i=0; i<5; i++){
  if (i == led){
    digitalWrite(leds[i], HIGH);
  }
  else{
    digitalWrite(leds[i], LOW);
  }
  }
  Serial.println(angles.y);
}

void twinkle(unsigned long current_time){
  float blink_speed = 0.5;
  int led;
  int brightness = int(float(current_time) / blink_speed) % 255;
 
  brightness = 255 - brightness;

  if (brightness > 200){
  led_switch = true;
  }

  Serial.print(led);
  Serial.print("\t");
  Serial.println(brightness);
 
  if (brightness < 10 && led_switch == true){
  led_switch = false;
  analogWrite(leds[led], 0);
  int led_new = random(5);
  while (led_new == led){
    led_new = random(5);
  }
  led = led_new;
  }

  for (int i = 0; i < 5; i++){
    if (i == led){
      analogWrite(leds[i], brightness);
    }
    else{
      analogWrite(leds[i], 0);
    }
  }  
}

void loop() {
  uint32_t t;
  t = millis();
  int second = (t % 1000) / 100;
  xyzFloat angles = myMPU9250.getAngles();

  if (mode == 0) {
    allOff();
  } else if (mode == 1) {
    allOn();
  } else if (mode == 2) {
    scanner(t);
  } else if (mode == 3) {
    alternate(second);
  } else if (mode == 4) {
    blinkLeds(second);
  } else if (mode == 5) {
    tilt(angles);
  } else if (mode == 6) {
    twinkle(t);
  }

}
