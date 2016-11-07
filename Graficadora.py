from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
import random


#class Graficadora(App):
class Graficadora(Widget):
    def build(self, NombreX, NombreY, Titulo, X, Y):
        self.opcion1 = 0
        self.opcion2=0
        self.wid = 0
        self.wid = Widget()
        self.principal = RelativeLayout()
        self.CanvaS = RelativeLayout()
        self.widget1 = Widget()
        self.CanvaS.size = 100, 100
        self.CanvaS.add_widget(self.widget1)
        self.principal.add_widget(self.CanvaS)
        self.CanvaS.add_widget(self.wid)
        self.Graficar(NombreX, NombreY, Titulo, X, Y)
        return self.principal
   
    def TituloGrafica(self, nombre):  
        with self.wid.canvas:
            lblX = Label()
            lblX.pos = 370, 280
            lblX.text = str(nombre)
            lblX.color = (0,0,0)
            self.wid.add_widget(lblX)
        
    def NombreY(self,  nombre):
        dispersa = Scatter()
        dispersa.pos = 109,-50
        dispersa.rotation=90
        with dispersa.canvas:
            lblY = Label()
            dispersa.add_widget(lblY)

            lblY.pos = 200,-50
            lblY.text = str(nombre)
            lblY.color = (0,0,0)

            self.wid.add_widget(dispersa)

    def NombreX(self,  nombre):
        with self.wid.canvas:
            lblX = Label()
            lblX.pos = 350,-37
            lblX.text = str(nombre)
            lblX.font_size = "4dp"
            lblX.color = (0,0,0)
            self.wid.add_widget(lblX)

    def desaparece(self, *args):
        if self.opcion2 == 0:
            pass
        if self.opcion2 ==1:
            self.CanvaS.remove_widget(wid)
            self.opcion1 = 1
#        wid.canvas.clear()

    def aparece(self, *args):
        if self.opcion1 == 0:
            self.dibu(self.wid)
            self.opcion2 = 1
            self.opcion1 = 2

        if self.opcion1==1:
            self.CanvaS.add_widget(self.wid)
            self.dibu(wid)
            self.opcion1=2

        if self.opcion1 ==2:
            pass



   
    def Plano(self,  *args):
        with self.wid.canvas:
            Color(225, 255, 255, 1.0, mode='rgba')
            Rectangle(pos=(200,0), size=(400,350))
            
            
    def ejesEspaciales(self,  *args):
        with self.wid.canvas:
          #  Color(225, 255, 255, .1, mode='rgba')
            Color(0,0,0)
            Line(points=[200, 40, 600, 40], width=1)
            Line(points=[240, 0, 240, 285], width=1)

    def Puntos(self, PuntoX, PuntoY, *args):
        d = 6
        with self.wid.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            #            Color(1,0,0)
   #         x =random.randint(240,600)
    #        y = random.randint(40,280)
            Ellipse(pos=( PuntoX- d / 2, PuntoY - d / 2), size=(d, d))

    
    def Llamarpuntos(self, cX, cY, *args):
        x, y = self.Escalar(cX, cY)
        self.Puntos(x,y)

    def LineasX(self):
        with self.wid.canvas:            
            Color(0,0,0)
            for i in range(0,65, 1):
                x = i*6.1538
                Line(points=[210+x, 35, 210+x, 45], width=1)
		z = i%5
		if (z==0):
                    Line(points=[210+x, 35, 210+x, 45], width=1.5)	

    def LabelX(self):
        with self.wid.canvas:            
            Color(0,0,0)
            for i in range(0,12, 1):
                x = i*30
                texto = str(5*i)
                escrito = "lbl"+str(i)
                escrito = Label()
                escrito.pos = 190 + x, -23
                escrito.text = str(texto)
                escrito.font_size= '9sp'
                escrito.color = (0,0,0)
                self.wid.add_widget(escrito)


    def LabelY(self):
        with self.wid.canvas:            
            Color(0,0,0)
            for i in range(-1,6, 1):
                y = i*40.71
                texto = str(i)
                escrito = "lbl"+str(i)
                escrito = Label()
                escrito.pos = 179, y
                escrito.text = str(texto)
                escrito.size_hint= .1,.1
                escrito.font_size= '9sp'
                escrito.color = (0,0,0)
                self.wid.add_widget(escrito)


    def LineasY(self):
        with self.wid.canvas:            
            Color(0,0,0)
            for i in range(0,70, 1):
                y = i*4.07
                Line(points=[235, 0+y, 245, 0+y], width=1)
		z = i%10
		if (z==0):
                    Line(points=[235, 40+y, 245, 40+y], width=1.5)
#                    Line(points=[210+x, 35, 210+x, 45], width=1.5)
        
    def Escalar(self, xi, yi):
        XE = 240 + (xi*360)/200
        YE = 40 + (yi*240)/5000
        return XE, YE

    def Graficar(self, NombreX, NombreY, Titulo, X,Y, *args):
        with self.wid.canvas:
            self.Plano()
            self.LineasX()
            self.LineasY()
            self.LabelX()
            self.LabelY()
            self.ejesEspaciales()
            self.NombreX(NombreX)
            self.NombreY( NombreY)
            self.TituloGrafica(Titulo)
            self.Llamarpuntos(X,Y)


#if __name__ == '__main__':
 #   MyPaintApp().run()

#pain = Graficadora().run()
