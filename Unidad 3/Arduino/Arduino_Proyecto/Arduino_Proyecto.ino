
int v;
int sensores []= {A0,A1,A2}; //Sensores digitales o analogicos: temperatura, luz, distancia: trigger y echo
int valores_Sensores []= {A0, A1, A2};

int actuadores[] = {6, 11,12};  //Poner los 3: servomotor, led, buzzer activo

//_______________________________________________________________________
void setup() 
{
Serial.begin(9600);
Serial.setTimeout(100);
for (int i = 0; i < 3; i++) //Activar los actuadores como salida
{
  pinMode(actuadores[i], OUTPUT);
}

}
//_______________________________________________________________________
int sensor1() {
  return analogRead(sensores[0]); 
}
int sensor2() {
  return analogRead(sensores[1]); 
}
int sensor3() {
  return analogRead(sensores[2]); 
}

void loop() {

// Sensores, envia las lecturas a python
  valores_Sensores[0] = sensor1();
  valores_Sensores[1] = sensor2();
  valores_Sensores[2] = sensor3();
  char cadena[30];
  sprintf(cadena, "%d@%d@%d@", valores_Sensores[0], valores_Sensores[1], valores_Sensores[2]);
  Serial.println(cadena);

// Actuadores, recibe de python
  if (Serial.available() > 0) //Hay algun dato
  {

  String comando = Serial.readStringUntil('\n');  // lee hasta salto de línea
    Serial.print("Comando recibido: ");
  Serial.println(comando);
  int separador = comando.indexOf('@');           // busca posición del @
  if (separador != -1) 
  {
    int indice = comando.substring(0, separador).toInt();
    int valor = comando.substring(separador + 1).toInt();

      if (indice >= 0 && indice < 3)
      {
        digitalWrite(actuadores[indice], valor);
      }
  }
  }

  delay(100);
}
