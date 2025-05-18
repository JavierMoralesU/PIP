int pot=A0;
int led=6;   

void setup(){

}

void loop()
{
int v=analogRead(pot); //0-1023
v=v/4; //map(v,0,1023,0,255)
analogWrite(led,v); //o-255
delay(10);
}