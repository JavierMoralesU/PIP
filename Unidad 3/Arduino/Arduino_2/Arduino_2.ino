void setup() {
  // put your setup code here, to run once:
// P2 IMP.Numeros_UART
Serial.begin(9600);

}

byte valor=0;

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(valor);
valor+=1;
delay(100); // ms

}
