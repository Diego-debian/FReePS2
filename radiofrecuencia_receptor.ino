/*
RECEPTOR
Apaga el LED 13 si recibe el mensaje "Apagar"
Enciende el LED 13 si recibe el mensaje "Encender"
*/
 
#include <VirtualWire.h> //incluimos la libreria virtualwire
#define Motorpin1  2
#define  Motorpin2  3
#define  Motorpin3  4
#define  Motorpin4  5
const int  led1 =13;
const int  led2 =8;
int valor;
int var1;
int Variable = 1;
int Var2 = 1;
int detener = 10;

//Definimos algunas variables necesarias para el envío del mensaje
//Estas variables vienen definidas en la libreria VirtualWire
byte message[VW_MAX_MESSAGE_LEN];
byte messageLength = VW_MAX_MESSAGE_LEN;

void setup()
{
  pinMode(led1, OUTPUT); //Configuramos el pin 13 como salida
  pinMode(led2, OUTPUT); //Configuramos el pin 13 como salida

  //Serial.begin(9600);  //Iniciamos la comunicacion serial
  vw_setup(2000);      //Iniciamos la comunicacion con el modulo RF
  vw_rx_start();       //Iniciamos la recepcion de datos
  //Serial.println("Receptor iniciado");
  pinMode(Motorpin1, OUTPUT);
  pinMode(Motorpin2, OUTPUT);
  pinMode(Motorpin3, OUTPUT);
  pinMode(Motorpin4, OUTPUT);
  
}
void loop()
{
  digitalWrite(led1, HIGH);
  digitalWrite(led2, HIGH);
  delay(50);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  delay(50);

  if (vw_get_message(message, &messageLength)) //Si recibimos un mensaje
  {
      if(comparar("Adelante") == 0){         //y es igual a ENCENDER
      LED1();      
      }
      else if(comparar("Atras") == 0)             //y si es igual a APAGAR
      { 
      LED2();      
      }
   else if(comparar("LED1") == 0)             //y si es igual a APAGAR
      { 
        LED1();      
      }
         else if(comparar("LED2") == 0)             //y si es igual a APAGAR
      { 
        LED2();      
      }
  }
} 
 
//Esta funcion compara el array de datos recibidos con los comandos para ejecutar ordenes
//Si son iguales, devuelve 1. Si no, devuelve 0.
char comparar(char* cadena) {
  for(int i = 0; i<messageLength; i++)
  {
    if(message[i] != cadena[i])
    {
      return 1;
    }
  }
  return 0;
}


void Paso()
{
  var1=Variable;
  while(Variable<=Var2)
{
 for (int i= 0; i<8; i++)
  {
  //desplazamiento total 1,985815602 mm, cada avance es de 0,24822695 mm
  delay(detener);
  Motor_ade();
  delay(detener);
  }
  Variable=Variable+1;
};
Variable = var1;

}

void Paso2()
{
  var1=Variable;
  while(Variable<=Var2)
{
  //desplazamiento total 1,985815602 mm, cada avance es de 0,24822695 mm
  for (int i= 0; i<8; i++)
  {
  delay(detener);
  Motor_ata();
  delay(detener);
  }  
  Variable=Variable+1;
};
Variable = var1;
}

void Motor_ade()
{
    //PASO1 
      digitalWrite(Motorpin1, HIGH);
      digitalWrite(Motorpin2, LOW);
      digitalWrite(Motorpin3, HIGH);
      digitalWrite(Motorpin4, LOW);
      delay(detener);

        //PASO2
      digitalWrite(Motorpin1, HIGH);
      digitalWrite(Motorpin2, LOW);
      digitalWrite(Motorpin3, LOW);
      digitalWrite(Motorpin4, HIGH);
      delay(detener);

        //PASO3 
      digitalWrite(Motorpin1, LOW);
      digitalWrite(Motorpin2, HIGH);
      digitalWrite(Motorpin3, LOW);
      digitalWrite(Motorpin4, HIGH);
      delay(detener);      

        //PASO4 
      digitalWrite(Motorpin1, LOW);
      digitalWrite(Motorpin2, HIGH);
      digitalWrite(Motorpin3, HIGH);
      digitalWrite(Motorpin4, LOW);
      delay(detener);  
   
   
}


void Motor_ata()
{
    //paso1 
      digitalWrite(Motorpin1, LOW);
      digitalWrite(Motorpin2, HIGH);
      digitalWrite(Motorpin3, HIGH);
      digitalWrite(Motorpin4, LOW);
      delay(detener); 

     //paso2
     digitalWrite(Motorpin1, LOW);
      digitalWrite(Motorpin2, HIGH);
      digitalWrite(Motorpin3, LOW);
      digitalWrite(Motorpin4, HIGH);
      delay(detener);   

       
           //PASO3
      digitalWrite(Motorpin1, HIGH);
      digitalWrite(Motorpin2, LOW);
      digitalWrite(Motorpin3, LOW);
      digitalWrite(Motorpin4, HIGH);
      delay(detener);


        //PASO4 
      digitalWrite(Motorpin1, HIGH);
      digitalWrite(Motorpin2, LOW);
      digitalWrite(Motorpin3, HIGH);
      digitalWrite(Motorpin4, LOW);
      delay(detener);
     
}

void Detener()
{
 // Serial.print("Estoy detenido");
 // Serial.print("\t");
  digitalWrite(Motorpin1, LOW);
  digitalWrite(Motorpin2, LOW);
  digitalWrite(Motorpin3, LOW);
  digitalWrite(Motorpin4, LOW);
  delay(detener);
}

void LED1()
{
  Paso();
  digitalWrite(led1, HIGH);
  delay(50);
  digitalWrite(led1, LOW);
  delay(50);
  
}

void LED2()
{
  Paso2();
  digitalWrite(led2, HIGH);
  delay(50);
  digitalWrite(led2, LOW);
  delay(50);
  
}