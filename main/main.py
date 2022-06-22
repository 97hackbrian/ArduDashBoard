##########################      GRUPO DINAMITA          ####################################
###MODULOS###
import serial,time,collections
import matplotlib.pyplot as plt
import matplotlib.animation as animacion
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
from tkinter import *
import numpy as np
from PIL import Image,ImageTk,ImageSequence
#############

###variables globales####
mensaje=''
b=0

#region Serial
########## CONEXION MEDIANTE EL PROTOCOLO SERIAL ###############
try:
        ard=serial.Serial("/dev/ttyUSB0",2000000,timeout=5);
        print("CONEXION CORRECTA")
        mensaje='ARDUINO CONECTADO'
        
        

except:
        print("NO SE PUDO CONECTAR")
        mensaje='ARDUINO NO CONECTADO'
###############################################################
#endregion Serial



#region Window
######### CONFIGURACIÓN DE LA VENTANA PRINCIPAL #################
window = Tk()
window.config(bg = "black")
window.geometry("1200x700")
window.title("DASHBOARD")
window['bg'] = '#171910'
################################################################
#endregion Window



#region Wallpaper
#-------------------------------------------------------------------------------------------------------------------------------------
#WALLPAPER
imag=PhotoImage(file="fondo.png")
imag = imag.zoom(2)
imag = imag.subsample(1)
back=Label(window,image=imag)
back.place(x=0,y=0)
#-------------------------------------------------------------------------------------------------------------------------------------
#endregion Wallpaper



#region FirstFuntion
#SEQUENCE FUNTIONS
#-------------------------------------------------------------------------------------------------------------------------------------
def binario(nn):
        bina=list(bin(nn))
        bina.pop(0)
        bina.pop(0)
        bin_int = [int(i) for i in bina]
        if len(bina)==1:
                bin_int.insert(0,0)
                bin_int.insert(0,0)
                bin_int.insert(0,0)
        elif len(bina)==2:
                bin_int.insert(0,0)
                bin_int.insert(0,0)
        elif len(bina)==3:
                bin_int.insert(0,0)
        return(bin_int)
def apagado():
        ard.write(b'4');
        ard.write(b'5');
        ard.write(b'6');
        ard.write(b'7');
def ledsec1():
	print("boton 1")
	for i in range (0,8):
		arr = bytes(str(i), 'utf-8')
		ard.write(arr);
                 #print(type(arr))
		time.sleep(1)
def ledsec2(s):
        global mensaje
        lim=0
        if s==1:
                
                lim=8
        else:
                try:
                        lim=int(entr.get())+1
                        
                        consola('EJECUTANDO...........')
                except:
                        print("oh nooo!")
                        consola('No es un número!')
                        time.sleep(3)
        for decimal in range (0,lim):
                lista_bin=binario(decimal)
	        #print("binario",lista_bin)
                for bandera in range (0,len(lista_bin)):
                                #print("La posicion es",bandera)        
                        if lista_bin[bandera]==1:
                                arr= bytes(str(bandera), 'utf-8')
                                ard.write(arr);
                                        #print(bandera)
                        else:
                                aux=bandera+4
                                        #print(aux)
                                arr= bytes(str(aux), 'utf-8')
                                ard.write(arr);
                time.sleep(2)
                apagado()
        consola('EJECUTADO')
#-------------------------------------------------------------------------------------------------------------------------------------
#endregion FirstFuntion



#region SecondFuntion
#MOTOR FUNTIONS
#------------------------------------------------------------------------------------------------------------------------------------
#GIF
i=Image.open('half.gif')
d=Image.open('all.gif')
def play_gif(d2):
        try:
                img2=d2
                for img2 in ImageSequence.Iterator(img2):
                        img2=img2.resize((130,130))
                        img2=ImageTk.PhotoImage(img2)
                        lbl.config(image=img2)
                        window.update()
                        time.sleep(0.03)
        except:
                print("cerrando Todo")
def NoSpeed():
        global tkTop
        global ard
        ard.write(bytes('N', 'UTF-8'))
def HalfSpeed():
        global tkTop
        global i
        global ard
        ard.write(bytes('H', 'UTF-8'))
        play_gif(i)
        lbl.config(image=imgs)
def MaximunSpeed():
        global tkTop
        global d
        global ard
        try:
                ard.write(bytes('M', 'UTF-8'))
                play_gif(d)
                lbl.config(image=imgs)
        except:
                print("cerrando")
                NoSpeed()
#-------------------------------------------------------------------------------------------------------------------------------------
#Region SecondFuntion



#region ThirdFuntion
#PLOT FUNTIONS
#-------------------------------------------------------------------------------------------------------------------------------------
isReceiving= False 
isRun = True 
datos = 0.0

muestraD = 500
data = collections.deque([0]*muestraD, maxlen=muestraD)
xmin = 0
xmax = muestraD
ymin = 0
ymax = 150 

def Iniciar():
        global ard
        global mensaje
        try:
                ard=serial.Serial("/dev/ttyUSB0",2000000,timeout=5);
                print("CONEXION CORRECTA")
                mensaje='ARDUINO CONECTADO'      
        except:
                print("NO SE PUDO CONECTAR")
                mensaje='ARDUINO NO CONECTADO'
        #ard.write(b'x')
        global datos
    
        global isReceiving
        global isRun
        isReceiving = True
        isRun = True
        try:
                thread.start() 
        except:
                print("Esta corriendo")
        #print(ard.readline().decode('utf-8'))
        anim = animacion.FuncAnimation(fig, plotData,  fargs=(muestraD,lines),interval = 100, blit = False )
        plt.grid()
        plt.show()
def DatosA():
        time.sleep(1)
        ard.reset_input_buffer() 
        while (isRun):
                global datos
                global isReceiving
                datos = float(ard.readline().decode('utf-8'))
                isReceiving=True
def plotData(self,muestraD,lines):
    data.append(datos)
    lines.set_data(range(muestraD), data)
    #print(datos)
    leds(int(datos))

thread = Thread(target = DatosA) 

fig = plt.figure(facecolor="0.55",figsize=(8, 4.5), clear=True, dpi=100)
ax = plt.axes(xlim=(xmin,xmax),ylim=(ymin,ymax))
plt.title("Grafica - 0 - 150 cm",color='white',size=16)
ax.set_xlabel("Muestras")
ax.set_ylabel("Distancia")
lines = ax.plot([] ,[], 'r')[0]
def Limpiar():
    fig.clf()

#LEDs With sensor FUNTIONS
class CircleButton:
    def __init__(Self, canvas, x, y, *, anchor="nw", **kwargs):
        # creo la imagen en x, y con el anchor dado por el usuario.
        # Si quieres que el centro del botón esté en ese punto, pasa el argumento anchor="center".
        Self.id = canvas.create_image(x, y, anchor=anchor, **kwargs)

        # Creo el atributo canvas y guardo el canvas allí, para poder usarlo después. Los objetos en el canvas se modifican usando métodos del canvas.
        Self.canvas = canvas
def leds(dis):
        #print(dis)
        if dis<=25:
                CircleButton(canvasL1, 50,50, anchor="center", image=led1ON)

        else:
                CircleButton(canvasL1, 50, 50, anchor="center", image=led1OFF)
        
        if dis<=50:
                CircleButton(canvasL2, 50,50, anchor="center", image=led1ON)
        else:
                CircleButton(canvasL2, 50,50, anchor="center", image=led1OFF)
        if dis<=75:
                CircleButton(canvasL3, 50,50, anchor="center", image=led1ON)
        else:
                CircleButton(canvasL3, 50,50, anchor="center", image=led1OFF)
        if dis<=100:
                CircleButton(canvasL4, 50,50, anchor="center", image=led1ON)
        else:
                CircleButton(canvasL4, 50,50, anchor="center", image=led1OFF)
#------------------------------------------------------------------------------------------------------------------------------------
#endregion ThirdFuntion



#region Other
#------------------------------------------------------------------------------------------------------------------------------------
def consola(mensaje):
        bin_num['text']=mensaje
        window.update()
def Salir():
        global isRun
        isRun = False
        global ard
        try:
                thread.join()

        except:
                print("Cerrando...")
        NoSpeed()
        ard.close()
        time.sleep(2)
        window.destroy()
        window.quit()
        print("proceso finalizado")
#------------------------------------------------------------------------------------------------------------------------------------
#endregion Other



#region Imagenes
#-----------------------------------------------------------------------
#IMAGENES EXTRA
img = Image.open('boton1.png')
img = img.resize((90, 90), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

img1 = Image.open('boton2.png')
img1 = img1.resize((85, 50), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

led1ON = Image.open('ledEncendido.png')
led1ON=led1ON.resize((90,90),Image.ANTIALIAS)
led1ON = ImageTk.PhotoImage(led1ON)

led1OFF = Image.open('ledApagado.png')
led1OFF=led1OFF.resize((90,90),Image.ANTIALIAS)
led1OFF = ImageTk.PhotoImage(led1OFF)

logo=Image.open('log.png')
logo = logo.resize((300, 150), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

imgs = Image.open('giff.gif')
imgs = imgs.resize((130, 130), Image.ANTIALIAS)
imgs = ImageTk.PhotoImage(imgs)
#-------------------------------------------------------------------------------------------------------------------------------------
#endregion Imagenes



#region Frames
#-------------------------------------------------------------------------------------------------------------------------------------
ploteo=Frame(window,bg='#061E6A',width=800,height=340,highlightbackground='gray25',highlightthickness=1)
ploteo.grid(padx=10,pady=7,row=1,columnspan=5,rowspan=5,sticky='nsew')

ploteo.grid_propagate(False)
ploteo.config(relief = "sunken")
ploteo.config(cursor = "heart")

ledf=Frame(window,bg='#061E6A',width=800,height=170,highlightbackground='gray25',highlightthickness=1)
ledf.grid(padx=1,pady=5,row=7,columnspan=3,rowspan=4,sticky='nsew')

ledc=Frame(window,bg='#061E6A',width=310,height=140,highlightbackground='gray25',highlightthickness=1)
ledc.grid(padx=5,pady=5,row=7,column=3,columnspan=3,rowspan=4,sticky='ew')

logoL=Label(ledc, image=logo,width=300,height=140,bg='black')
logoL.place(x=0,y=0)

disp=Frame(window,bg='#061E6A',width=90,height=140,highlightbackground='gray25',highlightthickness=1)
disp.grid(padx=5,pady=1,row=5,column=6,columnspan=3,rowspan=6,sticky='nsew')
#---------------------------
#endregion Frames



#region Canvas
#-------------------------------------------------------------------------------------------------------------------------------------
lienzo = FigureCanvasTkAgg(fig, master = ploteo )
lienzo._tkcanvas.grid(row = 0,column = 1, padx = 1,pady = 1)

canvasL1 = Canvas(ledf, highlightthickness=0,bg='#061E6A',width=100,height=100)
canvasL1.grid(row=0,column=0, padx=1,pady=1)

canvasL2 = Canvas(ledf, highlightthickness=0,bg='#061E6A',width=100,height=100)
canvasL2.grid(row=0,column=1, padx=1,pady=1)

canvasL3 = Canvas(ledf, highlightthickness=0,bg='#061E6A',width=100,height=100)
canvasL3.grid(row=0,column=2, padx=1,pady=1)

canvasL4 = Canvas(ledf, highlightthickness=0,bg='#061E6A',width=100,height=100)
canvasL4.grid(row=0,column=3, padx=1,pady=1)
#-------------------------------------------------------------------------------------------------------------------------------------
#endregion Canvas



#region Botones
#-------------------------------------------------------------------------------------------------------------------------------------
#Boton de secuencia simple
boto1 = Button(window,bg='#061E6A',font=('Ubuntu',10),text='SECUENCIA', image=img,relief='flat',activebackground='#0E297F',borderwidth=5,compound='center',fg='white',command=ledsec1)
boto1.grid(padx=5,pady=5,column=7,row=1)
#Boton de conteo numerico en binario
boto2 = Button(window,bg='#061E6A',font=('Ubuntu',10),text='BINARIOS', image=img,relief='flat',activebackground='#0E297F',borderwidth=5,compound='center',fg='white',command=lambda:ledsec2(1))
boto2.grid(padx=5,pady=5,column=7,row=2)

boto4 = Button(window,bg='#061E6A',font=('Ubuntu',10),text='NO SPEED', image=img,relief='flat',activebackground='#0E297F',borderwidth=5,compound='center',fg='white',command=NoSpeed)
boto4.grid(padx=5,pady=5,column=6,row=1)
boto5 = Button(window,bg='#061E6A',font=('Ubuntu',10),text='HALF SPEED', image=img,relief='flat',activebackground='#0E297F',borderwidth=5,compound='center',fg='white',command=HalfSpeed)
boto5.grid(padx=5,pady=5,column=6,row=2)
boto6 = Button(window,bg='#061E6A',font=('Ubuntu',10),text='MAX SPEED', image=img,relief='flat',activebackground='#0E297F',borderwidth=5,compound='center',fg='white',command=MaximunSpeed)
boto6.grid(padx=5,pady=5,column=6,row=3)

#Boton para iniciar la toma de datos
boto3 = Button(disp,bg='#061E6A',font=('Ubuntu',12,'bold'),text='RESET', image=img1,relief='flat',activebackground='#0E297F',activeforeground='red',borderwidth=5,compound='center',fg='black',command=Iniciar)
boto3.place(x=50,y=110)
exit = Button(disp,bg='#061E6A',font=('Ubuntu',12,'bold'),text='SALIR', image=img1,relief='flat',activebackground='#0E297F',activeforeground='red',borderwidth=5,compound='center',fg='black',command=Salir)
exit.place(x=210,y=110)

b_ans=Button(disp,bg='#061E6A',font=('Ubuntu',10),text='SEND',relief='flat',activebackground='#0E297F',borderwidth=5,
compound='center',fg='white',command=lambda:ledsec2(2))
b_ans.place(x=280,y=37)
#---------------------------------------------------------------------------------------------------------------------------------------
#endregion Botones



#region Titulos
#-------------------------------------------------------------------------------------------------------------------------
texto = "MOTOR"
etiqueta = Label(window,text=texto,bg='#061E6A',fg='white')
etiqueta.grid(padx=40,pady=5,column=6,row=0)
etiqueta.config(font=('Ubuntu',20,'bold')) 

texto1 = "GRAFICA"
etiqueta1 = Label(window,text=texto,bg='#061E6A',fg='white',compound='center')
etiqueta1.grid(padx=10,pady=1,column=0,row=0)
etiqueta1.config(font=('Ubuntu',20,'bold')) 

texto2 = "SECUENCIAS"
etiqueta2 = Label(window,text=texto2,bg='#061E6A',fg='white')
etiqueta2.grid(padx=5,pady=5,column=7,row=0)
etiqueta2.config(font=('Ubuntu',20,'bold')) 

texto3 = "LEDS"
etiqueta3 = Label(window,text=texto3,bg='#061E6A',fg='white')
etiqueta3.grid(padx=20,pady=5,column=0,row=6)
etiqueta3.config(font=('URW Gothic',20,'bold')) 

texto5 = "DISPLAY"
etiqueta5 = Label(window,text=texto5,bg='#061E6A',fg='white')
etiqueta5.grid(padx=20,pady=15,column=6,row=4)
etiqueta5.config(font=('URW Gothic',25,'bold'))
#-------------------------------------------------------------------------------------------------------------------------
#endregion Titulos



#region Display
#-------------------------------------------------------------------------------------------------------------------------
global entr
tit=Label(disp,text='INGRESE EL NÙMERO LÌMITE',font=('Ubuntu',15,'bold'),fg='white',bg='#061E6A')
tit.place(x=20,y=5)
entr=Entry(disp,font=("Ubuntu",15))
entr.place(x=20,y=40)

bin_num=Label(disp,text=mensaje,bg='#061E6A',font=('Ubuntu',10,'bold'),fg='white')
bin_num.place(x=20,y=80)

lbl=Label(window,bg='black',image=imgs)
lbl.grid(padx=0,pady=0,row=3,column=7)
#-------------------------------------------------------------------------------------------------------------------------
#endregion Display



window.rowconfigure(3, weight=2)
window.rowconfigure(1, weight=2)
window.rowconfigure(2, weight=2)
window.minsize(width=1200,height=700)
window.rowconfigure(1,weight=1)
window.columnconfigure(7,weight=1)
window.maxsize(width=1200,height=700)

window.mainloop()