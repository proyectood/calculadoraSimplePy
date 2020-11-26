from tkinter import *

vtn = Tk()
vtn.title("Calculadora")
vtn.geometry('235x150')
vtn.configure(background='black')

def suma():
    suma = int(txt1.get())+int(txt2.get())
    return resultado.set(suma)
def Resta():
    Resta = int(txt1.get())-int(txt2.get())
    return resultado.set(Resta)
def Multi():
    Multi = int(txt1.get())*int(txt2.get())
    return resultado.set(Multi)
def Divi():
    Divi = int(txt1.get())/int(txt2.get())
    return resultado.set(Divi)
def cerrar():
    vtn.destroy()

resultado = StringVar()


lbl1 = Label(vtn,text="Primer número",bg='black',fg='white')
lbl1.grid(row=1,column=1)
txt1 = Entry(vtn)
txt1.grid(row=1,column=2)
lbl2 = Label(vtn,text="Segundo número",bg='black',fg='white')
lbl2.grid(row=2,column=1)
txt2 = Entry(vtn)
txt2.grid(row=2,column=2)

btnSuma = Button(vtn,text="+",bg='yellow',fg='black',width=11,command=suma)
btnSuma.grid(row=3,column=1)
btnResta = Button(vtn,text="-",bg='yellow',fg='black',width=11,command=Resta)
btnResta.grid(row=3,column=2)
btnMulti = Button(vtn,text="x",bg='yellow',fg='black',width=11,command=Multi)
btnMulti.grid(row=4,column=1)
btnDivi = Button(vtn,text="/",bg='yellow',fg='black',width=11,command=Divi)
btnDivi.grid(row=4,column=2)

btnCerrar = Button(vtn,text="Cerrar",bg='red',fg='white',width=30,command=cerrar)
btnCerrar.grid(row=5,column=1,columnspan=2)

lblRes = Label(vtn,bg='white',width=30,textvariable=resultado)
lblRes.grid(row=6,column=1,columnspan=2)








vtn.mainloop()