
int led=13;

void setup() {
// P2 IMP.Numeros_UART

pinMode(led,OUTPUT);
Serial.begin(9600);
Serial.setTimeout(10);//ms
}

int v;

void loop() {
  // put your main code here, to run repeatedly:

if (Serial.available()>0){
  v=Serial.readString().toInt();
  digitalWrite(led,v);
}
delay(100);
}
