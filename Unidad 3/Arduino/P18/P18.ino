int led = 13;

void setup() {
  //put your setup code here, to run once:
    pinMode(led,OUTPUT);
    Serial.begin(9600);
    Serial.setTimeout(100);
}

int valor;
void loop() {
//put your main code her, to run repeatedly:
if (Serial.available()>0){
   valor = Serial.readString().toInt();
   digitalWrite(led,valor);
}
}



