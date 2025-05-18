
int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;


void setup() {
// P2 IMP.Numeros_UART

pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(led4,OUTPUT);


Serial.begin(9600);
Serial.setTimeout(10);//ms
}

int v;

void loop() {
  // put your main code here, to run repeatedly:

if (Serial.available()>0)
{
  v=Serial.readString().toInt();
  ApagarLeds();
  digitalWrite(v,5); //Capaz no es 5

}
delay(100);
}

void ApagarLeds()
{
   digitalWrite(led1,0);
   digitalWrite(led2,0);
   digitalWrite(led3,0);
   digitalWrite(led4,0);
  delay(100);
}
