
int led = 13;

void setup() {
  // put your setup code here, to run once:
// P2 IMP.Numeros_UART
//Serial.begin(9600);
pinMode (led,OUTPUT);//OUTPUT Actuadores
                     //INPUT

}

void loop() {
  // put your main code here, to run repeatedly:

digitalWrite(led,1);// ms

delay(250);

digitalWrite(led,0);

delay(250);
}
