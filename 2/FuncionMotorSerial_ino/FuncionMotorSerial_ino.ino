const int pwma = 5;
const int ain2 = 6;
const int ain1 = 7;




int incomingByte;

void setup(){
  
  Serial.begin(2000000);
  
  pinMode(pwma, OUTPUT);
  pinMode(ain2, OUTPUT);
  pinMode(ain1, OUTPUT);

}

void loop(){
  if(Serial.available() > 0){
    incomingByte = Serial.read();
    if(incomingByte == 'N'){
      apagado();
      analogWrite(pwma,0);
      
    }
    if(incomingByte == 'H'){
      velmed();
      analogWrite(pwma,128);
      
    }
    if(incomingByte == 'M'){
      velmax();
      analogWrite(pwma,255);
      
    }
  }
}

void apagado(){
  digitalWrite(ain2,0);
  digitalWrite(ain1,0);
}

void  velmed(){
  digitalWrite(ain2,0);
  digitalWrite(ain1,1);
}

void velmax(){
  digitalWrite(ain2,0);
  digitalWrite(ain1,1);
}
