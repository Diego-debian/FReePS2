#-*- coding:utf-8 -*-
#qpy:kivy
'''
Aplicación desarrollada en Bogotá D.C.; Colombia
	Licenciado en física ---------------------------------> Diego Alberto Parra Garzón     DESARROLLADOR DE CONTENIDO 
	semillero Fisifor Universidad Distrital
	grupo Hack-vision y opensai
	
'''
import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from commands import getoutput
import ArduinoBluetooth
from kivy.graphics import Color, Ellipse, Rectangle, Line
from ArduinoBluetooth import *
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from kivy.core.window import Window 
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from presentacion import *
import os 

import os
import time
kivy.require('1.9.0')
class FReePS(App):
    def Label1(self):
        global lbl1
        img2 = Image()
        img2.source = "img/text.png"        
        #        img2.pos = 215, 140
        img2.pos = 400, 160
        img2.size= 400, 500
        lbl1 = Label()
        lbl1.text =  "Esperando instrucciones:"
        #   lbl1.pos = 200,140
        lbl1.pos = 530,380
        lbl1.font_size = "14dp"
        Mprincipal.add_widget(img2)
        Mprincipal.add_widget(lbl1)
        print "Esperando instrucciones:"

    def Label2(self):
        widget3 = Widget()
        img2 = Image()
        img2.source = "img/text.png"        
        x,y = 50, 330
        img2.pos = x, y-160
        img2.size= 300, 500
        lbl2 = Label()
        lbl2.pos = x+90 , y+40
        lbl2.font_size= '18dp'
        lbl2.text = "   " + 'FReePS DEMO\n        Diego Alberto Parra  \n'+ "          "+'             Bogota D.C.'
        widget3.add_widget(img2)
        widget3.add_widget(lbl2)  
        Mprincipal.add_widget(widget3)

    def Label3(self, *args):
        global MascaraDatos
        print "2"
        global Mdatos
        Mdatos = Widget()
        MascaraDatos = Widget()
        print "3"
        print "4"
        Mensaje1 = "Longitud: \n"+ str(self.Longitud) + " (m)"
        print "5"
        Mensaje2 = "Frecuencia: \n"+ str(self.Frecuencia) +" (Hz)"
        print "6"
        Mensaje3 = "F. angular: \n"+ str(self.fangular) +" (rad/s)"
        print "7"
        Mensaje4 = "Periodo: \n"+ str(self.periodo)+ " (s)"
        print "8"
        print Mensaje1, "\n", Mensaje2, "\n", Mensaje3, "\n", Mensaje4
        print "9"
        print "12"
        lblz1 = Label(text=Mensaje1, pos = (480, 10), font_size = "12dp")
        print "13"
        lblz2 = Label(text=Mensaje2, pos=(480,-30), font_size = "12dp")
        print "14"
        lblz3 = Label(text=Mensaje3, pos = (580, 10), font_size = "12dp")
        print "15"
        lblz4 = Label(text=Mensaje4, pos=(580,-30), font_size = "12dp")
        print "16"
        MascaraDatos.add_widget(lblz1)
        print "17"
        MascaraDatos.add_widget(lblz2)
        print "18"
        MascaraDatos.add_widget(lblz3)
        print "19"
        MascaraDatos.add_widget(lblz4)
        print "20"
        with Mdatos.canvas:
            print "10"
            Color(1,0,0,.5, mode='rgba')
            print "11"
            Rectangle(pos=(470,0), size=(240,80))

        Mdatos.add_widget(MascaraDatos)
        Mprincipal.add_widget(Mdatos)

    
    def BotonSalir(self):
        Mascara = RelativeLayout()
        wid = Widget()
        Btn = Button()
        Btn.pos = 720, 210
        Btn.size = 80, 50
        Btn.text = "Salir"
        Btn.bind(on_press = self.Salir)
        wid.add_widget(Btn)
        Mascara.add_widget(wid)
        Mprincipal.add_widget(Mascara)

    def Salir(self, *args):
        exit()
    
    def BluetoothLIN(self, *args):
        global linuxBluetooth
        import serial
        lecpuerta = getoutput("rfcomm")
        lectura = lecpuerta.split(":")
        puerta = lectura[0]
        puerta = "/dev/"+str(puerta)
        print puerta
        linuxBluetooth = serial.Serial(puerta, 9600)
        linuxBluetooth.write("44") 


    def pasoENBlIN(self):
        try:
            lbl1.text = "Espere conectando el Bluetooth"
            self.BluetoothLIN()           
            Mensaje = "Dispositivo conectado"
            print Mensaje
            lbl1.text = Mensaje 
        except:
            Mensaje = "Dispositivo NO CONECTADO revise su conexion "
            print Mensaje
            self.BluetoothLIN()
            pass
        pass

    def pasoEMB(self, *args):
        try:
            Dispo = "HC-05"
            lbl1.text = "Espere conectando el Bluetooth"
            ArduinoB.obtenerCorrienteEnchufe(Dispo)
            Mensaje = "Dispositivo conectado"
            print Mensaje
            lbl1.text = Mensaje 
        except:
            Mensaje = "Dispositivo NO CONECTADO revise su conexion "
            print Mensaje
            ArduinoB.obtenerCorrienteEnchufe("HC-05")
            lbl1.text = Mensaje
            pass


    def EncenderBluetooth(self, *args):
        print "Llamado a prender"
        try: 
            self.pasoEMB()
        except:
            pass
        try:
           self.pasoENBlIN()

        except:
            print "que paso recoño"

            pass
            
        pass
    def ApagarBluetooth(self, *args):
        try:
            ArduinoB.Cerrar()
            Mensaje = "Conexion cerrada"
            print Mensaje 
            lbl1.text = Mensaje

        except:
            Mensaje = "Revise su conexion"
            print Mensaje
            lbl1.text = Mensaje


    def pasoEBlue1(self, Mensaje, *args):
        try:
            ArduinoB.Escribir(Mensaje)
            Mensaje1 = "Se envio el mensaje ["+Mensaje+"]\n correctamente."
            print Mensaje1
            lbl1.text = Mensaje1
        except:
            Mensaje1 =  "Fallo el envio del mensaje ["+Mensaje+"]\n  revise su conexion."
            pass

    def pasoEBlue2(self, Mensaje, *args):
        try:
            Mensaje1 = "Se envio el mensaje ["+Mensaje+"]\n correctamente."
            print Mensaje1
            lbl1.text = Mensaje1
            linuxBluetooth.write(Mensaje)
        except: 
            Mensaje1 =  "Fallo el envio del mensaje ["+Mensaje+"]\n revise su conexion."
            pass
    
    def EscribirBluetooth(self, Mensaje, *args):
        try:
            self.pasoEBlue1(Mensaje)

        except:
            pass

        try:
            self.pasoEBlue2(Mensaje)

        except:
            pass
   

    def Lel1(self, *args):
        try:
            print "esta leyendo"
            Lec1 = ArduinoB.LeerNUMERO()
            lel = float(Lec1)
            self.yl = lel
        except:
            pass

    def Lel2(self, *args):
        try:
            Lec1 = linuxBluetooth.readline()            
            lel = float(Lec1)
            self.yl = lel
        except: 
            pass
        
    def Lectura(self, *args):
        try:
            self.Lel1()
        except:
            pass
        try:
            self.Lel2()
        except:
            pass



    # IDENTIFICADOR DE PROCESOS EN ARDUINO
    def ProcesosArduino(self):
        try:
            global ArduinoB
            print "Llamado a la libreria"
            from ArduinoBluetooth import *
            
            print "paso el llamado"
            print "instanciando la clase ArduinoBluetooth"
            ArduinoB = ArduinoBluetooth()
            Mensaje = "Todos los procesos Arduino Activados "
            print Mensaje 
            lbl1.text = Mensaje
            
        except:
            Mensaje = "Fallo al activar los\n procesos Arduino"
            print Mensaje
            lbl1.text = Mensaje

        try: 
            print "Revizando la lectura\n del Bluetooth"
            self.EncenderBluetooth()
            print "Lectura correcta"
            Mensaje = "Todos los procesos\n Arduino Activados "
            print Mensaje 
            lbl1.text = Mensaje
        except:
            Mensaje = "Fallo La Lectura del\n bluetooth"
            print Mensaje
            lbl1.text = Mensaje
        pass




    def Dispersion2(self):
        self.dis2 = Scatter()
        self.dis2.pos =  -90, -50
        #self.dis2.pos =  random.randrange(100,680), 100
        self.dis2.size_hint = None,None
        #      self.dis2.size = 86, 86
        self.dis2.do_rotation= False
        self.dis2.do_scale= False
        self.dis2.do_translation= False
        self.dis2.rotation = 0
        self.dis2.scale= 1.7

    def Camara(self, *args):
        self.Dispersion2()
        global cam
        camwidget = Widget()  #Create a camera Widget
        cam = Camera()        #Get the camera
        cam.resolution=(640,480)
        cam.size= 1000,800
        cam.pos=(-100,-100)
        cam.play=True         #Start the camera
        camwidget.add_widget(cam) 
        self.dis2.add_widget(camwidget)
        #        Mprincipal.add_widget(self.dis2)
        MCamara.add_widget(self.dis2)

    def BotonPresentacion(self):
        global Mascarapresenta
        Mascara = RelativeLayout()
        wid = Widget()
        Btn = Button()
        #    Btn.background_normal =  'img/observa.png'
        Btn.text = "Dudas"
        Btn.pos = 720, 160
        Btn.size = 80, 50
        Btn.bind(on_press = self.presentaopcion)
        wid.add_widget(Btn)
        Mascara.add_widget(wid)
        Mprincipal.add_widget(Mascara)


    def presentaopcion(self, *args):
        self.pasoboton1=1
        if (self.presentaX == 1):
            pass
        if (self.pasoboton1==1):        
            pass
        if (self.pasoboton1==0):
            pass

        if (self.presentaX == 0):
            self.Presentacion()
            self.presentaX = 1



    def Presentacion(self): 
        global presenta
        self.Mascara2P.pos= 0,0
        presenta = presentacion().build(0)
        self.Mascara2P.add_widget(presenta)


    def BotonCamara(self):
        Mascara = RelativeLayout()
        wid = Widget()
        Btn = Button()
        #    Btn.background_normal =  'img/observa.png'
        Btn.text = "Foto"
        Btn.pos = 720, 60
        Btn.size = 80, 50
        Btn.bind(on_press = self.TomarFoto)
        wid.add_widget(Btn)
        Mascara.add_widget(wid)
        Mprincipal.add_widget(Mascara)

    def btnlike(self):
        Mascara = RelativeLayout()        
#        Mascara.size = 40,40
        wid = Widget()
        Btn = Button()
        #  Btn.text= "Inicio"
        #    Btn.background_normal =  'img/like.png'
        #Sensor 1 Sensor de electrorrecepcion activa
        Btn.text = "Sensor1"
        Btn.pos = 720, 110
        Btn.size = 80, 50
        Btn.bind(on_press = self.Paso_boton1)
        wid.add_widget(Btn)
        Mascara.add_widget(wid)
        Mprincipal.add_widget(Mascara)

    def btnEx(self):
        Mascara = RelativeLayout()
#        Mascara.size = 40,40
        wid = Widget()
        Btn = Button()
       # Btn.text= "Inicio"
     #  Btn.background_normal =  'img/quit.png'
        Btn.pos = 720, 10
        Btn.size = 80, 50
        Btn.text = "Detener"
        Btn.bind(on_press = self.Paso_boton2)
        wid.add_widget(Btn)
        Mascara.add_widget(wid)
        Mprincipal.add_widget(Mascara)

    def Paso_boton1(self, *args):
        self.presentaX = 1
        if (self.presentaX==1):
            pass
        if (self.presentaX==0):
            pass

        if (self.pasoboton1==1):
            pass

        if (self.pasoboton1 == 0):
            os.system("rm sensor.dat")
            self.accionesbtnlike()
            self.pasoboton1 = 1
            self.pasoboton2 = 1



    def Paso_boton2(self, *args):
        if (self.pasoboton2 == 1 ) or (self.presentaX==1):
            self.accionesbtnEx()
            self.pasoboton1 = 0
            self.pasoboton2 = 1

        if (self.pasoboton2==0):
            pass


    def accionesbtnEx(self, *args):
        #Probar si se puede detener la funcion graficar
        try:
            Clock.unschedule(self.GraficarAhora)
        except:
            pass

        #Probar si se puede remover la grafica del widget principal
        try:            
            Mprincipal.remove_widget(Mascara1)
        except:
            pass
        #Probar si se puede detener los procesos del modulo motorizado
        try:
            self.EscribirBluetooth("44")
            Mprincipal.remove_widget(lbl1)
            self.Mascara2P.remove_widget(presenta)
            MCamara.remove_widget(Mprincipal)
            self.presentaX = 0
            #            MCamara.remove_widget(self.layMasc)            
            MCamara.add_widget(Mprincipal)
            Mprincipal.add_widget(lbl1)
        except:
            pass
        

        try:
            self.PROCESOS()
        except:
            pass

        try:
            self.BufferDatos()
            self.estadoAnteX = 240
            self.estadoAnteY = 40
            self.pasoboton1 = 0
            self.pasoboton2 = 0
            self.presentaX = 0
            self.Y=0

            Mprincipal.remove_widget(textoScroll)
            Mprincipal.remove_widget(vistaScroll)
        except:
            pass

        pass


    def accionesbtnlike(self, *args):
        global Mascara1
        Mascara1 = RelativeLayout()
        Mascara1.pos= -150,0
        from Graficadora import *
        grap = Graficadora().build("Timpo en (s)", "Diferencia de potencial (V)", "Tiempo  vs Diferencia de potencial ", 0,  0)
        Mascara1.add_widget(grap)
        Mprincipal.add_widget(Mascara1)     
        self.EscribirBluetooth("6")
        self.tiempoInicial = time.time()
        print self.tiempoInicial
        self.BufferDatos()
        print "Paso el scrool"
        Clock.schedule_interval(self.GraficarAhora, 1/25)

    def Adhiere_scroll(self, *args):
        try:
            x = self.TF
            y = self.Y
            y =str(y)
            x = str(x)
            btnz = Label(text=x, size_hint_y=None, height=30)
            btnxz = Label(text=y, size_hint_y=None, height=30)
            MascaraS.add_widget(btnz)
            MascaraS.add_widget(btnxz)
        except:
            pass
    
    def CicloUtil(self,x,y, *args):
        if (x <= 50.0):
            if (y>5000):
                pass
            if (y<=5000):
                self.GrafAnimada(x, y) 
                self.guardarDatos(x,y)
                pass

        if (x > 50.0):
            Clock.unschedule(self.GraficarAhora)
            Clock.unschedule(self.Adhiere_scroll)
            self.EscribirBluetooth("44")             
            self.Y = 0
            print self.datosSalvados
            self.SCROLL()
            self.exportarDatos()
 #           self.AnalizaDatos()


    
    def LongitudCuerda(self, h):
        print "cuerda 1"
        print "h es:", type(h), h
        h  = float(h)
        Frecuencia = h/50.0
        print "cuerda 2", Frecuencia
        Periodo = 50/h
        print "cuerda 3"
        gravedad = 9.81
        print "cuerda 4"
        calculo1 = Frecuencia*2*self.PI
        calculo2 = calculo1*calculo1        
        Longitud = gravedad/calculo2
        Mensaje = "La longitud de la cuerda es: ", Longitud, " (m)"
        print "cuerda 9"
        print  Mensaje
        self.Longitud = Longitud
        print "esta es la longitud: ", self.Longitud
        self.Frecuencia= Frecuencia
        print "esta es la frecuencia: ",self.Frecuencia
        self.fangular= calculo1
        print "Esta es la fecuencia angular: ",self.fangular
        self.periodo = Periodo
        print "Este es el periodo", self.periodo    
        estado1 = self.Longitud
        estado2 = self.Frecuencia
        estado3 = self.fangular
        estado4 = self.periodo
        try:
            self.Longitud = round(self.Longitud, 3)
        except:
            self.Longitud = estado1
        try:
            self.Frecuencia = round(self.Frecuencia, 3)
        except:
            self.Frecuencia = estado2
        try:
            self.fangular = round(self.fangular, 3)
        except:
            self.fangular = estado3
        try:
            self.periodo = round(self.periodo, 3)
        except:
            self.periodo = estado4
            
        try:
            self.Label3()
        except:
            print "No se colocaron las imagnes de los datos"
            pass

        print "cuerda 10"
        pass

        
        
        
    def AnalizaDatos(self, *args):
        print "Comienza l"
        l = self.datosSalvados
        print "este era l" , l
        m = len(l)  
        
        print "empieza m: ", m
        try:
            for i in range(0,m,1):
                xl = self.datosSalvados[i][0]
                y0 = self.datosSalvados[i-3][1]
                y1 = self.datosSalvados[i-2][1]
                y2 = self.datosSalvados[i-1][1]
                yp = self.datosSalvados[i][1]
                y4 = self.datosSalvados[i+1][1]
                y5 = self.datosSalvados[i+2][1]
                #         y5 = self.datosSalvados[i+2][1]
                #        y6 = self.datosSalvados[i+3][1]
                
                if ((y0<y1)&(y1 < y2)&(y2<yp)&(yp>y4)&(y4>y5)):
                    self.analisisdatos.append([xl, yp])
                    #    print self.analisisdatos

                else:
                    print "No hay coincidencia"
                    h = len(self.analisisdatos)
                    print self.analisisdatos
                    print h
                try:
                    self.LongitudCuerda(h)
                except:
                    pass

        except: 
            pass

            

 
    def GraficarAhora(self, *args):        
        print "Empezo la grafica"

        try:
            print "1"
            lbl1.text=        "REVISE EL BLUETOOTH"
            self.Lectura()
            self.Y = self.yl
            self.deltaTiempo = time.time()
            self.tiempoFinal = self.deltaTiempo-self.tiempoInicial
            print self.tiempoFinal
            self.TF = round(self.tiempoFinal, 3)
            lbl1.text=        "Algo 7"
            print "8"
            MEnsaje = "            Captura de datos  \n"
            print "9"
            lbl1.text= MEnsaje + " Tiempo (s): "+ str(self.TF) + "\n  Voltaje (mV): "+ str(self.Y)
            print "10"
            self.CicloUtil(self.TF, self.Y)


        except:
            pass
                
     
        pass

    def Escalar(self, xi, yi):
        XE = 240 + (xi*360)/60
        YE = 40 + (yi*245)/5000
        return XE, YE


    def GrafAnimada(self, PuntoX, PuntoY):
        x, y = self.Escalar(PuntoX, PuntoY)
        d = 4
        with Mascara1.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            Ellipse(pos=(x- d / 2, y - d / 2), size=(d, d))
            nuevoEstaX = x - d /2
            nuevoEstaY = y - d/2
            Line(points=[self.estadoAnteX, self.estadoAnteY , x, y], width=1)
            self.estadoAnteX = nuevoEstaX
            self.estadoAnteY = nuevoEstaY


    def TomarFoto(self, *args):
        try:
            Window.screenshot(name='../../../../../mnt/sdcard/DCIM/imagen.png')
            pass
        except:
            print "No se pudo tomar  la foto"  
            pass
 #           pass
        try:
            Window.screenshot(name='imagen.png')
            pass
        except:
            print "No se pudo tomar  la foto"  
            pass

        try:
          #  Window.screenshot(name='captura.png')
  
            Window.screenshot(name='../../../../../storage/sdcard1/Picture/captura.png')
            pass
        
        except:
            Window.screenshot(name='../../../../../storage/sdcard0/Picture/captura.png')    
            pass


        pass

    def guardarDatos(self, x, y, *args):
        self.datosSalvados.append([x,y])


    def exportarDatos(self, *args):
        self.guardaDATO = 0
        m = self.datosSalvados
        z = len(m)
        self.m = z
        self.RectanguloScroll()
        Clock.schedule_interval(self.exportDATA, 1/50)

    def exportDATA(self, *args):
        if (self.guardaDATO < self.m):
            self.BufferexportDATA()

        if (self.guardaDATO >= self.m):
            Clock.unschedule(self.exportDATA)
            print "llamando a la funcion analisis"
            self.AnalizaDatos()
            print "se llamo al analisis"
            
        

    def BufferexportDATA(self, *args):
        i = self.guardaDATO
        xl = self.datosSalvados[i][0]
        yl = self.datosSalvados[i][1]
        xo = str(xl)
        yo = str(yl/1000)
        self.TF = xo
        self.Y = yo
        self.Adhiere_scroll()
        print "paso ", xo, " ", yo
        archi = open('sensor.dat', 'a+')
        archi.write (xo)
        archi.write ("\t")
        archi.write (yo)
        archi.write("\n")
        archi.close()
        self.guardaDATO = i + 1





    def BufferDatos(self, *args):
        self.datosSalvados = []
        self.analisisdatos = []



    def ProcesosCamara(self):
        try:
            self.Camara()
        except:
            print "Fallo la activacion de la camara"
        try:
            self.BotonCamara()
            print "Procesos de la camara se activaron" 
        except:
            pass
            #self.BotonCamara()
            
        pass

    def RectanguloScroll(self):
        with textoScroll.canvas:
            Color(1,0,0,.5, mode='rgba')
            Rectangle(pos=(470,100), size=(240,190))

        lblz = Label(text="Tiempo (s)", pos = (490, 230))
        lblxz = Label(text="Voltaje (V)", pos=(610,230))
        textoScroll.add_widget(lblz)
        textoScroll.add_widget(lblxz)

    def SCROLL(self, *args):
        global MascaraS
        global vistaScroll
        global textoScroll
        textoScroll = Widget()
        MascaraS = GridLayout(cols=2, spacing=2, size_hint_y=None, size_hint_x = None, size=(250,100))
        # Make sure the height is such that there is something to scroll.
        MascaraS.bind(minimum_height=MascaraS.setter('height'))
        vistaScroll = ScrollView(size_hint=(None, None), size = (260,150))
        vistaScroll.add_widget(MascaraS)
        vistaScroll.pos = 465, 105
        #root.size = 20, 40

        Mprincipal.add_widget(textoScroll)
        Mprincipal.add_widget(vistaScroll)
        

    def ProcesosKivy(self):
        self.Label1()
        self.Label2()
        #      self.Label3()
        self.BotonPresentacion()
        self.btnlike()
        self.btnEx()
        self.BotonSalir()

    def PROCESOS(self):
#        try:
 #           self.ProcesosCamara()
  #          print "Camara Iniciada"
   #     except: 
    #        print "Fallo al activar la camara"
        try:
            MCamara.add_widget(Mprincipal)

            self.ProcesosKivy()
            print "Procesos Kivy Activados"
        except:
            print "Fallo al activar los procesos kivy"

        try:
            self.ProcesosArduino()
            print "Procesos arduino activados"
            #          lbl1.text="Procesos arduino activados"
        except:
            print "Fallo al activar los procesos Arduino"
        pass
        
        try:
            self.Mascara2P = Widget()
            self.layMasc = RelativeLayout()
            self.layMasc.add_widget(self.Mascara2P)
            Mprincipal.add_widget(self.layMasc) 
        except: 
            print "Error de Mascara 2P"

 #   def VariablesGlobales(self):

    def build(self):
        self.pasoboton1 = 0
        self.pasoboton2 = 0
        self.presentaX = 0
        self.PI = 3.14159265
        global MCamara
        global Mprincipal
        self.estadoAnteX = 240
        self.estadoAnteY = 40
        #        self.VariablesGlobales()
        MCamara = RelativeLayout()
        Mprincipal = Widget()
        self.ProcesosCamara()

        self.PROCESOS()
        #       return Mprincipal
        return MCamara

if __name__=='__main__':
    FReePS().run()
    
