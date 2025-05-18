
int v;
int sensor = A0;
void setup() {

Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  v = analogRead(sensor);
  Serial.println("V. Sensor: "+ String(v));
  delay(100);
}
