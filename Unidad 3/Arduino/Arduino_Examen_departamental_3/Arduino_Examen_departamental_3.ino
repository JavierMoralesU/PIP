

#include <Servo.h>


bool modoLuzAutomatico = true;
int sensor[] = {3, 4}; //Sensor de distancia: trigger y echo
int actuador = 6; //servomotor

// Objetos
Servo miServo;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);

  // Inicializar sensores
  pinMode(sensor[0], OUTPUT); //Distancia trigger
  pinMode(sensor[1], INPUT); //Distancia echo

  // Inicializar actuadores
  miServo.attach(actuador); //Servo
}



long leerDistancia() {
  digitalWrite(sensor[0], LOW);   // TRIG
  delayMicroseconds(2);
  digitalWrite(sensor[0], HIGH); //Enciende el pulso muy poco tiempo, 10 microsegundos
  delayMicroseconds(10);
  digitalWrite(sensor[0], LOW);
  //ECHO
  long duracion = pulseIn(sensor[1], HIGH, 30000); // ECHO,  30000 microsegundos = 30 milisegundos
  
  if (duracion == 0) { // No se detectó nada, retornar un valor alto, que se consideraria fuera del rango del sensor, y por ende de las graficas
    return 500; 
  }
  
  long distancia = duracion * 0.034 / 2; //Velocidad de sonido entre 2, ir y volver
  return distancia;
}
void moverServoTemporal(int angulo) { // 90° como base
  miServo.write(angulo);
}



void loop() {

// Sensores, envia las lecturas a python en formato "lecturaDistancia@ " ,Valores de 0-400 cm de distancia
long distancia = leerDistancia();
char cadena[40];
sprintf(cadena, "%ld@", distancia);
Serial.println(cadena);


// Actuadores, recibe mensaje "@valor" desde python

  if (Serial.available() > 0) 
  {
    String comando = Serial.readStringUntil('\n');
    int separador = comando.indexOf('@');
    if (separador != -1) 
    {
      int valor = comando.substring(separador + 1).toInt();
      moverServoTemporal(valor); // mueve a 180° grados durante x milisegundos
    }
  }

  delay(100);
}
