
String resp;

void setup() {
// P2 IMP.Numeros_UART
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

if (Serial.available()>0){
  resp=Serial.readString();//timeout default
  Serial.print(resp);
}
delay(100);
}
