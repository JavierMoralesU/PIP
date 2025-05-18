int pot= A0;

int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;
int led5 = 9;
int led6 = 10;
int led7 = 11;
int led8 = 12;

void setup() {

Serial.begin(9600);
//No requiere pinMode
}

void loop() {


  int v= analogRead(pot);
  delay(100);

  if (v<500) {

  digitalWrite(led1, 1);
  delay(200);
  digitalWrite(led1, 0);
  delay(200);

  digitalWrite(led2, 1);
  delay(200);
  digitalWrite(led2, 0);
  delay(200);
 }

}
