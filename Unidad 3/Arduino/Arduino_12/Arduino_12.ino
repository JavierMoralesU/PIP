int pot= A0;

void setup() {
// P2 IMP.Numeros_UART

Serial.begin(9600);
//No requiere pinMode
}

void loop() {

  int v= analogRead(pot);
  Serial.println(v);
  delay(100);
}
