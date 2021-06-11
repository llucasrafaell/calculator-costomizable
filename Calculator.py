
import webbrowser
from tkinter import *
from selenium import webdriver

root = Tk()
root.resizable(False, False)
root.geometry('280x380')
root.title('Calculator.py')

def menu():

    menu =Tk()
    menu.resizable(False, False)
    menu.geometry('600x150')
    menu.title('Personalize')
    textspace = Text(menu)
    textspace.place(x=0, y=0)
    textspace.configure(font=("Georgia", 12))

def openLink():
    webbrowser.open('https://github.com/llucasrafaell')

def clickButtom(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual)+ str(numero))

def clickPonto():
    visor.insert(END,'.')

def delete():
    visor.delete(0, END)

def clickAddition():
    first_num = visor.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_num)
    visor.delete(0, END)

def clickMinus():
    first_num = visor.get()
    global f_num
    global math
    math = 'minus'
    f_num = float(first_num)
    visor.delete(0, END)

def clickDiv():
    first_num = visor.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_num)
    visor.delete(0, END)

def clickMult():
    first_num = visor.get()
    global f_num
    global math
    math = 'multiply'
    f_num = float(first_num)
    visor.delete(0, END)

def clickIgual():
    second_num = visor.get()
    visor.delete(0, END)
    if math == 'addition':
        visor.insert(0, f_num + float(second_num))
    if math == 'minus':
        visor.insert(0, f_num - float(second_num))
    if math == 'multiply':
        visor.insert(0, f_num * float(second_num))
    if math == 'division':
        visor.insert(0, f_num / float(second_num))

def search():
    record_question = entry_question.get()
    navegador = webdriver.Chrome()
    navegador.get("https://brainly.com.br/")
    request_question = navegador.find_element_by_xpath('//*[@id="hero-search"]')
    request_question.click()
    request_question.send_keys(record_question)
    get_question = navegador.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/div[1]/div/form/div/div/button')
    get_question.click()
    print(record_question)

b0 = Button(root,text = '0', bg='lightgreen', pady=14, padx=64, bd=4, command = lambda: clickButtom(0))
b1 = Button(root,text = '1', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(1))
b2 = Button(root,text = '2', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(2))
b3 = Button(root,text = '3', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(3))
b4 = Button(root,text = '4', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(4))
b5 = Button(root,text = '5', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(5))
b6 = Button(root,text = '6', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(6))
b7 = Button(root, text ='7', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(4))
b8 = Button(root,text = '8', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(8))
b9 = Button(root,text = '9', bg='lightgreen', pady=14, padx=14, bd=4, command = lambda: clickButtom(9))

b0.place(x=10,y=265)
b1.place(x=10,y=210)
b2.place(x=60,y=210)
b3.place(x=110,y=210)
b4.place(x=10,y=155)
b5.place(x=60,y=155)
b6.place(x=110,y=155)
b7.place(x=10, y=100)
b8.place(x=60,y=100)
b9.place(x=110,y=100)

#visor
visor = Entry(root, bg='lightgreen')
visor.place(x = 40, y = 10, width=200, height=40)

#operações
button_division = Button(root,text = '/', bg='lightgreen', pady=10, padx=10, bd=4, command = clickDiv)
button_multiply= Button(root,text = '*', bg='lightgreen', pady=10, padx=10, bd=4, command = clickMult)
button_minus = Button(root,text = '-', bg='lightgreen', pady=10, padx=10, bd=4, command = clickMinus)
button_addition = Button(root,text = '+', bg='lightgreen', pady=28, padx=9, bd=4, command = clickAddition)

button_division.place(x=160,y=100)
button_multiply.place(x=160,y=145)
button_minus.place(x=160,y=190)
button_addition.place(x=160,y=237)

#outros
button_ce = Button(root,text = 'CE', bg='lightgreen', pady=42, padx=22, bd=4, command = delete)
button_equal = Button(root,text = '=', bg='lightgreen', pady=14, padx=25, bd=4, command = clickIgual)
button_dot = Button(root,text = '.', bg='lightgreen', pady=14, padx=27, bd=4, command = clickPonto)
button_github = Button(root,text = 'My GitHub!', bg='lightgreen', pady=14, padx=30, bd=4, font = ('verdana', 9, 'bold'), command = openLink)

button_ce.place(x=200,y=100)
button_equal.place(x=200,y=210)
button_dot.place(x=201,y=265)
button_github.place(x=10,y=320)

#personalize
bpersonalize = Button(root,text = 'Personalize', bg='lightgreen', pady=15, padx=11, font = ('verdana', 8, 'bold') , bd=4, command = menu)
bpersonalize.place(x=160,y=320)

#questions
label_question = Label(root, text ='Search solution ↓', font=("Georgia", 10))
label_question.place(x = 85, y=50)
entry_question = Entry(root, bg='lightgreen')
entry_question.place(x = 40, y = 70, width=200, height=20)
entry_question.configure(font=("Georgia", 10))
search_buttom = Button(root,text = '?', bg='lightgreen', pady=5, padx=5, bd=2, command = search)
search_buttom.place(x=245, y = 60)

root.mainloop()
