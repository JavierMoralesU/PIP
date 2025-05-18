void setup() {
  // put your setup code here, to run once:
// P2 IMP.Numeros_UART
Serial.begin(9600);

}

byte v=0;

void loop() {
  // put your main code here, to run repeatedly:
Serial.println("Valor"+ v);
v+=1;
delay(250); // ms

}
