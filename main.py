
from ast import Lambda
from tkinter import *
from turtle import bgcolor




raiz = Tk()
raiz.title("Calculadora Python")
miFrame = Frame(raiz)
miFrame.pack()
operacion = ""

resultado = int(0)


#pantalla
numeroPantalla=StringVar()
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)#columnspan adquiere el ancho de las columnas
pantalla.config(background="grey",fg ="purple",justify="right")

#pulsaciones teclados

def numeroPulsado(num:str):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion =""
    else:   
        numeroPantalla.set(numeroPantalla.get()+num)

def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion = suma
    numeroPantalla.set(resultado)

def el_resultado():
    global resultado 

    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0


def resta():
    pass
def dividir():
    pass
def multiplicar():
    pass

#fila 1 de botones

boton7 = Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7")).grid(row=2,column=1)
boton8 = Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8")).grid(row=2,column=2)
boton9 = Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9")).grid(row=2,column=3)
botonDiv = Button(miFrame,text="/",width=3,background="grey").grid(row=2,column=4)

#fila 2 de botones

boton4 = Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4")).grid(row=3,column=1)
boton5 = Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5")).grid(row=3,column=2)
boton6 = Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6")).grid(row=3,column=3)
botonMult = Button(miFrame,text="X",width=3,background="grey").grid(row=3,column=4)

#fila 3 de botones

boton1 = Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1")).grid(row=4,column=1)
boton2 = Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2")).grid(row=4,column=2)
boton3 = Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3")).grid(row=4,column=3)
botonRest = Button(miFrame,text="-",width=3,background="grey").grid(row=4,column=4)

#fila 4 de botones

boton0 = Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0")).grid(row=5,column=1)
botonComa = Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(",")).grid(row=5,column=2)
botonIgual = Button(miFrame,text="=",width=3,command=lambda:el_resultado()).grid(row=5,column=3)
botonSuma = Button(miFrame,text="+",width=3,background="grey",command=lambda:suma(numeroPantalla.get())).grid(row=5,column=4)



raiz.mainloop()
