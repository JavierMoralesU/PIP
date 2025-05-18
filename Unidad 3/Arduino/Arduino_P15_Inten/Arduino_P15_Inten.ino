int led=6;    

setup(){

}

loop()
{

for(int i=0; i<255;i++){
  analogWrite(led, i);
  delay(10);
}

for(int i=255; i>0; i--){
  analogWrite(led,i);
  delay(10);
}
}