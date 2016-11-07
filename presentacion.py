from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

class presentacion(RelativeLayout):

    def ControlImagenes(self, *args):

        if self.opcionimagen == 0:
            self.opcionimagen = self.opcionimagen+1
            self.ControlImagenes()
        else:
            print "Ronro"
            PasarImagen = "img/imagenes/freeps"+str(self.opcionimagen)+".png"
            self.IMAGEN.source = PasarImagen
            print PasarImagen
        
        
    def avanzaDer(self, *args):
        if (( self.opcionimagen <=6)&(self.opcionimagen>0)):
            self.opcionimagen = self.opcionimagen + 1
            self.ControlImagenes()
        else:
            pass

    def avanzaIzq(self, *args):
        if (( self.opcionimagen <=7)&(self.opcionimagen>0)):
            self.opcionimagen = self.opcionimagen - 1
            self.ControlImagenes()
        else:
            pass


    def IMAGENTUTORIAL(self):
        x,y = 430, 100
        widget3 = Widget()
        self.IMAGEN = Image()
        self.IMAGEN.pos =20,0     
        self.IMAGEN.size= 600, 350
        widget3.add_widget(self.IMAGEN)
        self.widget1.add_widget(widget3)    


    def BotonImagen6(self):
        wid2 = Widget()
        Btn6 = Button()
        Btn6.background_normal =  'img/dere.png'
        Btn6.pos = 550, -30
        Btn6.bind(on_press = self.avanzaDer)
        self.widget1.add_widget(Btn6)

    def BotonImagen7(self):
        wid2 = Widget()
        Btn7 = Button()
        Btn7.background_normal =  'img/izq.png'
        Btn7.pos = -10, -30
        Btn7.bind(on_press = self.avanzaIzq)
        self.widget1.add_widget(Btn7)


    def build(self, opcion):
	if (opcion== 0):
            self.opcionimagen=0
            self.widget1 = Widget()
            self.IMAGENTUTORIAL()
            self.ControlImagenes()
            self.BotonImagen6()
            self.BotonImagen7()
            return self.widget1
	else: 
            exit()

#esto = presentacion()
#esto.run()
