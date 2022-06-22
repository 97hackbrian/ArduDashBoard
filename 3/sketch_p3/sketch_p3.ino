const int hc05=4;
long t; //timepo que demora en llegar el eco
int d; //distancia en centimetros
void setup() {
  Serial.begin(115200);
  //Serial.println("ok1"); ////primero excepcion
}

int distancia(){
  
  pinMode(hc05,OUTPUT);
  digitalWrite(hc05, LOW);
  delayMicroseconds(2);         //Enviamos un pulso de 10us
  digitalWrite(hc05, HIGH);
  delayMicroseconds(10);
  digitalWrite(hc05, LOW);
  
  pinMode(hc05,INPUT);
  t = pulseIn(hc05, HIGH); //obtenemos el ancho del pulso
  d = (t * 0.034) / 2;             //escalamos el tiempo a una distancia en cm
  
  return d; //en cm
  
}

void loop() {
  delay(50);
  Serial.println(distancia());
}
