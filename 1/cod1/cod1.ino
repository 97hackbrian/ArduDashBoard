#define led1 9
#define led2 10
#define led3 11
#define led4 12
char in;
void setup() {                
  pinMode(led1, OUTPUT);     
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  Serial.begin(115200);
}

void loop(){
  while (Serial.available()) {
  in= Serial.read();
  //Serial.write(in);
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
}
