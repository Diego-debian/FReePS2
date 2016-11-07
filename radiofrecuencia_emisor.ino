/*
EMISOR
Envia los mensajes "Apagar" y "Encender" en intervalos de un segundo.
*/
#include <SoftwareSerial.h>
#include <VirtualWire.h> //incluimos la libreria virtualwire
#define RxD 6
#define TxD 7
#define pin_trig 13
#define pin_eco 12
int detener = 10;
int valor;
int var1;
int Variable = 1;
int Var2 = 1;
const int pin_envio = 10; 
const int  led =11;
const int sensor1 = A0;
const int sensor2 = A5;
const int ledEmisor = 8;
long miliVolts1;
long intensidad1;
long miliVolts2;
long intensidad2;
SoftwareSerial Blue(TxD, RxD);
void Intensidad1();
void Intensidad2();
void Sensor();
void Menu();

void setup()
{
  Blue.begin(9600);
  Serial.begin(9600); //Iniciamos la comunicacion serial
  vw_set_tx_pin(pin_envio);
  vw_setup(2000);  //Iniciamos la comunicacion con el modulo RF
  pinMode(led,OUTPUT);
  pinMode(pin_trig,OUTPUT);
  pinMode(pin_eco,INPUT);
  pinMode(ledEmisor,OUTPUT);
  pinMode(sensor1,INPUT);
  pinMode(sensor2,INPUT);

}
void loop()
{
Menu();
}
 
//Funcion para enviar el mensaje por RF
void send (char *message)
{
  vw_send((uint8_t *)message, strlen(message)); //Envia el mensaje
  vw_wait_tx(); //Espera hasta que se envien los datos
  
} 

void Sensor()
{
  digitalWrite(pin_trig, LOW);
  delayMicroseconds(2);
  digitalWrite(pin_trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pin_trig, LOW);
  
  float duracion;
  duracion = pulseIn(pin_eco, HIGH);
  double T;
  T = sqrt(290/270);
  //distancia en centimetros
  float distancia;
  distancia = (200.401*T/1000)*(duracion/2);
  Blue.print("\t");
  Blue.print(distancia);
  Blue.print("\t");
  Blue.print(duracion/2);
  Blue.print("\t");
  Blue.print("\r\n");
  delay(detener);  
}

void Intensidad1()  
{
  miliVolts1 = (analogRead(sensor1) *5000L) /1023; //opteniendo el valor sensor
  intensidad1 =miliVolts1;
  Blue.print("\t"); //salida al Serialporth
  Blue.print(intensidad1);
  Blue.print("\t");
  Blue.print("\r\n");
  delay(detener);
}

void Intensidad2()  
{
  miliVolts2 = ((analogRead(sensor2) *5000L) /1023)*2; //opteniendo el valor sensor
  intensidad2 =miliVolts2;
  Blue.print("\t"); //salida al Serialporth
  Blue.print(intensidad2);
  Blue.print("\t");
  Blue.print("\r\n");
  delay(detener);
}

void Menu()
{
//  valor = analogRead(A0);
 // valor = ((valor*5*100)/1023);
  digitalWrite(ledEmisor, LOW);
  char comando = Blue.read();
  switch(comando)
  {
   case '1':
             send("Adelante"); //Enviamos ENCENDER  
             Menu();
            break;
    case '2':
             send("Atras");   //Enviamos APAGAR
             Menu();

            break;  
  
    case '3':
            while(comando=='3')
            {
         //     Serial.println(valor);
              digitalWrite(led, HIGH);
              delay(125);
              digitalWrite(led, LOW);
              delay(125);
              Sensor();              
              Menu();
         
            }
            break;
  
    case '4':
            while(comando=='4')
            {
            //  Blue.print(valor);
             // Blue.print(" \r\n");
              digitalWrite(led, LOW);
              Menu();
            }
            break;  

     case '5':
      while(comando=='5')
            {
         //     Serial.println(valor);
              Intensidad1();              
              digitalWrite(led, HIGH);
              delay(100);
              digitalWrite(led, LOW);
              delay(100);
              Menu();
         
            }
            break;
     case '6':
      while(comando=='6')
            {
         //     Serial.println(valor);
              digitalWrite(ledEmisor, HIGH);
              Intensidad2();              
              digitalWrite(led, HIGH);
              delay(50);
              digitalWrite(led, LOW);              
              delay(50);
              Menu();         
            }
            break;            
  } 
}
