int led1 = 2;
int led2 = 3;
int led3 = 4;
int boton1 = 11;
int boton2 = 12;
int boton3 = 13;
int estado1;
int estado2;
int estado3;

void setup(){
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3 ,OUTPUT);
  pinMode(boton1, INPUT);
  pinMode(boton2, INPUT);
  pinMode(boton3, INPUT);
}
void loop(){
  estado1 = digitalRead(boton1);
  estado2 = digitalRead(boton2);
  estado3 = digitalRead(boton3);
  if(estado1 == 1){
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
   }
  if(estado2 == 1){
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
   }
  if(estado3 == 1){
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
   }
    
}
