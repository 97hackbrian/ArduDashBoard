import serial
import time
import tkinter

def NoSpeed():
    global tkTop
    varLabel.set("NO SPEED")
    ser.write(bytes('N', 'UTF-8'))
def HalfSpeed():
    varLabel.set("HALF SPEED")
    ser.write(bytes('H', 'UTF-8'))
def MaximunSpeed():
    varLabel.set("MAXIMUN SPEED")
    ser.write(bytes('M', 'UTF-8'))
 
#COM PORT CONFIGURATION
ser = serial.Serial('COM4', 2000000)
#print("Reset Arduino")  #Sin esto cuando ejecuto a veces se inicia el motor
#time.sleep(2)

#The UTF-8 is an econding protcol which is an standard in Spyder, that's why we only used .encode() method
#ser.write(bytes('H', 'UTF-8'))
 
tkTop = tkinter.Tk()
tkTop.geometry('900x400')
tkTop.title("MOTOR control")
 
#DISPLAY THE STATUS OF THE LED
varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel)
varLabel.set("MOTOR STATUS")
tkLabel.pack()
 
#ON BUTTON
button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop, text="NO SPEED", bg="#40CFFF", height = 5, width = 10, command=NoSpeed)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)
#button1state.grid(row=1,column=1)

#OFF BUTTON
button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop, text="HALF SPEED", bg="#40CFFF", height = 5, width = 10, command=HalfSpeed)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)
#button2state.grid(row=2,column=2)

#EXIT BUTTON
button3 = tkinter.IntVar()
button3state = tkinter.Button(tkTop, text="MAXIMUN SPEED", bg="#40CFFF", height = 5, width = 10, command=MaximunSpeed)
button3state.pack(side='top', ipadx=10, padx=10, pady=15)
#button3state.grid(row=3,column=3)

tkinter.mainloop()