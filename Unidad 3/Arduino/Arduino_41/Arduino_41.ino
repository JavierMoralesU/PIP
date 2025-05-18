int actuadores[] = {10,11,12};

void setup() {
for (int i=0; i<3; i++){
pinMode(actuadores[i], OUTPUT);
}
Serial.begin(9600);
Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0){
  String cadena = Serial.readString(); //
  Serial.print(cadena);
  //
  int led = cadena.charAt(0)-48;//
  int estado = cadena.charAt(1)-48;  
  Serial.print(String(led) + " " + String(estado));
  digitalWrite(actuadores[led], estado);
  }
  delay (100);
}