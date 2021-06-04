import webbrowser
from tkinter import *
root = Tk()
root.resizable(False, False)
root.geometry('280x380')
root.title('CALCULADORA em Python')

def OpenLink():
    webbrowser.open('https://github.com/llucasrafaell')

def clickButtom(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual)+ str(numero))

def clickPonto():
    visor.insert(END,'.')

def delete():
    visor.delete(0, END)

def clickSoma():
    primeiroNumero = visor.get()
    global pNumero
    global matematica
    matematica = 'soma'
    pNumero = float(primeiroNumero)
    visor.delete(0, END)

def clickMenos():
    primeiroNumero = visor.get()
    global pNumero
    global matematica
    matematica = 'subtracao'
    pNumero = float(primeiroNumero)
    visor.delete(0, END)

def clickDiv():
    primeiroNumero = visor.get()
    global pNumero
    global matematica
    matematica = 'divisao'
    pNumero = float(primeiroNumero)
    visor.delete(0, END)

def clickMult():
    primeiroNumero = visor.get()
    global pNumero
    global matematica
    matematica = 'multiplicacao'
    pNumero = float(primeiroNumero)
    visor.delete(0, END)

def clickIgual():
    segundoNumero = visor.get()
    visor.delete(0, END)
    if matematica == 'soma':
        visor.insert(0, pNumero + float(segundoNumero))
    if matematica == 'subtracao':
        visor.insert(0, pNumero - float(segundoNumero))
    if matematica == 'multiplicacao':
        visor.insert(0, pNumero * float(segundoNumero))
    if matematica == 'divisao':
        visor.insert(0, pNumero / float(segundoNumero))

lb1 = Label(root, text='CALCULADORA EM PY', font = ('verdana', 12, 'bold'), pady=10)
lb1.pack()

visor = Entry(root, bg='lightgreen')
visor.pack()

#fileira 1:
b7 = Button(root, text ='7', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(7))
b7.place(x=10, y=100)

b4 = Button(root,text = '4', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(4))
b4.place(x=10,y=155)

b1 = Button(root,text = '1', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(1))
b1.place(x=10,y=210)

#fileira 2:

b8 = Button(root,text = '8', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(8))
b8.place(x=60,y=100)

b5 = Button(root,text = '5', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(5))
b5.place(x=60,y=155)

b2 = Button(root,text = '2', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(2))
b2.place(x=60,y=210)

#fileira 3:

b9 = Button(root,text = '9', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(9))
b9.place(x=110,y=100)

b6 = Button(root,text = '6', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(6))
b6.place(x=110,y=155)

b3 = Button(root,text = '3', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(3))
b3.place(x=110,y=210)

#Botao 0:

b0 = Button(root,text = '0', bg='lightgreen', pady=14, padx=64, bd=4, command = lambda: clickButtom(0))
b0.place(x=10,y=265)

#Botao linkedin:

blkd = Button(root,text = 'Clica pra conferir o meu GitHub!!!', bg='lightgreen', pady=14, padx=33, bd=5, command = OpenLink)
blkd.place(x=10,y=320)

#Botao CE:

bce = Button(root,text = 'CE', bg='lightgreen', pady=42, padx=22, bd=4, command = delete)
bce.place(x=200,y=100)

#Botao IGUAL:

bigual = Button(root,text = '=', bg='lightgreen', pady=14, padx=25, bd=4, command = clickIgual)
bigual.place(x=200,y=210)

#Botao PONTO:

bponto = Button(root,text = '.', bg='lightgreen', pady=14, padx=27, bd=4, command = clickPonto)
bponto.place(x=201,y=265)

#Fileira 4:

bdiv = Button(root,text = '/', bg='lightgreen', pady=10, padx=10, bd=4, command = clickDiv)
bdiv.place(x=160,y=100)

bmult = Button(root,text = '*', bg='lightgreen', pady=10, padx=10, bd=4, command = clickMult)
bmult.place(x=160,y=145)

bmenos = Button(root,text = '-', bg='lightgreen', pady=10, padx=10, bd=4, command = clickMenos)
bmenos.place(x=160,y=190)

bmais = Button(root,text = '+', bg='lightgreen', pady=28, padx=9, bd=4, command = clickSoma)
bmais.place(x=160,y=237)

root.mainloop()
