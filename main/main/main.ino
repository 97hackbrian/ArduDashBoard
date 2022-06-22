#define led1 9
#define led2 10
#define led3 11
#define led4 12
/////////////////////
#define pwma 6
#define ain2 7
#define ain1 8

const int hc=2;
long t;
int d;
int incomingByte;
char in;

void setup() {                
  pinMode(led1, OUTPUT);     
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  /////////////////////
  pinMode(pwma, OUTPUT);
  pinMode(ain2, OUTPUT);
  pinMode(ain1, OUTPUT);
  
  Serial.begin(2000000);
}

void ledSec(char in){
  if (in=='0'){
  digitalWrite(led1, HIGH);
  }
  else if (in=='1'){
  Serial.write(in);
  digitalWrite(led2, HIGH);
  
  }
  else if (in=='2'){
  digitalWrite(led3, HIGH);
  
  }
  else if (in=='3'){
  digitalWrite(led4, HIGH);
  
  }
  if (in=='4'){
  digitalWrite(led1, LOW);
  
  }
  if (in=='5'){
  Serial.write(in);
  digitalWrite(led2, LOW);
  
  }
  if (in=='6'){
  digitalWrite(led3, LOW);
  
  }
  if (in=='7'){
  digitalWrite(led4, LOW);
  
  }
}

void motSec(char incomingByte){
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

/*
void Sen(char in){
  if(in=='x'){
    delay(100);
    while(true){
      delay(50);
      Serial.println(distancia());
      in=Serial.read();
      if(in=='x'){
        break;
      }
    }
  }
}
*/
void Sen(){
  delay(80);
  Serial.println(distancia());
}

int distancia(){
  
  pinMode(hc,OUTPUT);
  digitalWrite(hc, LOW);
  delayMicroseconds(2);
  digitalWrite(hc, HIGH);
  delayMicroseconds(10);
  digitalWrite(hc, LOW);
  
  pinMode(hc,INPUT);
  t = pulseIn(hc, HIGH); 
  d = (t * 0.034) / 2;             
  
  return d; //en cm
}

void loop(){
  while (Serial.available()) {
  in= Serial.read();
  ledSec(in);
  motSec(in);
  //Sen(in);
  }
  Sen();
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
