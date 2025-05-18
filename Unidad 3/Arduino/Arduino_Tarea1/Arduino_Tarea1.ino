//E01
int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;


void setup() {

pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(led4,OUTPUT);


Serial.begin(9600);
Serial.setTimeout(10);//ms
}

int v;

void loop() {

  digitalWrite(led1, 1);
  delay(200);
  digitalWrite(led1, 0);
  delay(200);

  digitalWrite(led2, 1);
  delay(200);
  digitalWrite(led2, 0);
  delay(200);

  digitalWrite(led3, 1);
  delay(200);
  digitalWrite(led3, 0);
  delay(200);

  digitalWrite(led4, 1);
  delay(200);
  digitalWrite(led4, 0);
  delay(200);

  digitalWrite(led4, 1);
  delay(200);
  digitalWrite(led4, 0);
  delay(200);

  digitalWrite(led3, 1);
  delay(200);
  digitalWrite(led3, 0);
  delay(200);

  digitalWrite(led2, 1);
  delay(200);
  digitalWrite(led2, 0);
  delay(200);

  digitalWrite(led1, 1);
  delay(200);
  digitalWrite(led1, 0);
  delay(200);
  


}

