#Программа выполняет перевод из 10-ой сс в 4-ую и обратно

from tkinter import *
root = Tk()                      #Создание окна
root.geometry('400x400')         #Размеры окна
root.configure(bg = '#C0C0C0')


def translate(root):          #Основная функция перевода чисел,также включает проверку на ввод
    lab = Label(text = '                                  ')
    lab.place(x = '170',y = '35')
    r1 = ent.get()
    q = len(r1)
    fak = 0
    w1 = m = m1 = m2 = fin1 =  p = 0
    w2 = w3 = fin2 = fin3 = 0
    if r1!='' and r1[0]=='-':             #Проверка числа на отрицательность
        r1 = r1[1:q:1]
        m = 1
        q = q - 1
        m1 = 1
    if r1!='' and r1.replace('.','',1).isdigit() and r1[0]!='.':    #Начало перевода
        r1 = float(r1)
        if r1%1>0:              #Если число дробное то отделяется целая и дробная части
            r2 = r3 = ''        #Перевод дробных чисел
            r1 = str(r1)
            q = len(r1)
            for i in range(q):
                if r1[i]=='.':
                    p1 = i
            r2 = r1[0:p1:1]
            r3 = r1[p1+1:q:1]
            for i in range(len(r2)):
                if r2[i]>'3':
                    fak = 1
            for i in range(len(r3)):
                if r3[i]>'3':
                    fak = 1
                    
            if var.get()==1 and fak==0:                  #Перевод в 10 сс
                q = len(r2)
                for i in range(q):
                    w2 = r2[i]
                    w2 = int(w2)
                    fin2 += w2*(4**(q-1-i))
                q = len(r3)
                for i in range(q):
                    w3 = r3[i]
                    w3 = int(w3)
                    fin3 += w3*(4**(-i-1))
                fin3 = str(fin3)
                fin3 = fin3[0:7:1]
                fin3 = float(fin3)
                fin2 = fin2 + fin3                
                if m==1:
                    fin2 = fin2*(-1)                                    
                listbox.insert(0,' =======================',\
                       'Введенное число в 4-ой сс:',ent.get(),\
                       'Результат перевода в 10-ую:',fin2)
            elif var.get()==1 and fak==1:
                    lab = Label(text = 'Неверный ввод',fg = 'red')         #Вывод надписи при некорректных входных данных
                    lab.place(x = '170',y = '35')
            elif var.get()==2:               #Перевод в 4 сс
                fin2 = []
                r2 = int(r2)
                while r2>0:
                    w2 = int(w2)
                    w2 = r2%4
                    w2 = str(w2)
                    fin2.insert(0,w2)
                    r2 = r2//4
                w3 = ''
                for i in range(len(fin2)):         
                    w4 = fin2[i]
                    w3 +=w4
                fin3 = ''
                q = len(r3)
                r3 = int(r3)
                r3 = r3/(10**q)
                while len(fin3)<3:
                    r3 = r3*4
                    w5 = r3//1
                    r3 = r3 - w5
                    w5 = int(w5)
                    w5 = str(w5)
                    fin3+=w5
                if w3=='':
                    w3 = '0'
                w3 = w3+'.'+fin3
                if m==1:
                    w3 = '-'+w3
                listbox.insert(0,' =======================',\
                       'Введенное число в 10-ой сс:',ent.get(),\
                       'Результат перевода в 4-ую:',w3)
                
                    
                    
            
        else:                  #Перевод целые числа
            r1 = ent.get()
            r1 = float(r1)
            r1 = str(r1)
            q = len(r1)
            if m1==1:           #Проверка на отрицательность
                r1 = r1[1:q:1]
            q = len(r1)
            for i in range(q):
                if r1[i]=='.':
                    q-=2
                    m2 = 1
            for i in range(q):
                if r1[i]>'3':
                    w1 = 1
            if var.get()==1 and w1==0:                 #Перевод в 10 сс
                for i in range(q):
                    w1 = r1[i]
                    w1 = int(w1)
                    fin1 += w1*(4**(q-i-1))                
                if m==1:
                    fin1 = -fin1
                listbox.insert(0,' =======================',\
                       'Введенное число в 4-ой сс:',ent.get(),\
                       'Результат перевода в 10-ую:',fin1)
            elif var.get()==1 and w1==1:
                    lab = Label(text = 'Неверный ввод',fg = 'red')         #Вывод надписи при некорректных входных данных
                    lab.place(x = '170',y = '35')
            elif  var.get()==2:                    #Перевод в 4 сс
                fin2 = []
                if m2==1:
                    r1 = r1[0:q:1]
                r1 = int(r1)
                while r1>0:
                    w2 = r1%4                             
                    w2 = str(w2)
                    fin2.insert(0,w2)
                    r1 = r1//4
                w3 = ''
                for i in range(len(fin2)):
                    w4 = fin2[i]
                    w3 +=w4
                r1 = ent.get()
                r1 = float(r1)
                if m==1 and r1!=0:
                    w3 = int(w3)
                    w3 = -w3
                elif r1==0:
                    w3 = 0
                else:
                    w3 = w3
                listbox.insert(0,' =======================',\
                               'Введенное число в 10-ой сс:',ent.get(),\
                               'Результат перевода в 4-ую:',w3)
    else:
        lab = Label(text = 'Неверный ввод',fg = 'red')         #Вывод надписи при некорректных входных данных
        lab.place(x = '170',y = '35')
        
            

def menu1():                               #Очищает все поле
    listbox.delete(0,END)
def menu2():                               #Очищает последнюю операцию
    listbox.delete(0,4)

def menu11(root):                          #Очищает все поле 
    listbox.delete(0,END)
def menu22(root):                          #Очищает последнюю операцию
    listbox.delete(0,4)

def menu3():                               #Основная функция перевода
    translate(root)
def menu5():                   #Выводим информацию об авторе и программе
    root2 = Tk()
    root2.geometry('443x98')
    lab1 = Label(root2,text='Воробьев Даниил.\n ИУ7-21Б \n Калькулятор перевода из десятичной системы счисления \n в четверичную и обратно.',
                  font='Arial 12')                             
    lab1.place(x=5, y=10)
    
    root2.mainloop()
def kn1(root):                       #kn1-kn10 - Функции для ввода с помощью кнопок
    ent.insert(END,root)



def del1(root):                    #Функция для очистки поля ввода
    ent.delete(0,END)
    

ent = Entry()                         #Строка ввода
ent.place(x = '170',y = '60')
ent.bind('<Return>',translate)

m = Menu(root)                          #Создаем падающее меню
root.config(menu = m)
fm = Menu(m)
m.add_cascade(label = 'Меню',menu = fm)
fm.add_command(label = 'Стереть всё',command = menu1)    
fm.add_command(label = 'Стереть последнее',command = menu2)
fm.add_command(label = 'Выполнить перевод',command = menu3)
fm.add_command(label = 'О программе',command = menu5)


var = IntVar()
rb1 = Radiobutton(root,text = 'В 10-ую',variable=var,value=1)  #Кнопки перевода
rb2 = Radiobutton(root,text = 'В 4-ую',variable=var,value=2)
rb1.place(x = '38',y = '90')
rb2.place(x = '38',y = '120')

but1 = Button(root,text = 'выполнить перевод',width = 20,height = 1) #Кнопка1
but1.place(x = '180',y = '5')
but1.bind('<Button-1>',translate)

but2 = Button(root,text = 'Очистить всё',width = 12,height = 1)     #Кнопка2
but2.place(x = '1',y = '190')
but2.bind('<Button-1>',menu11)

but3 = Button(root,text  = 'Удалить одну операцию',width = 22,height = 1)  #Кнопка3
but3.place(x = '1',y = '150')
but3.bind('<Button-1>',menu22)

but4 = Button(root,text = 'стереть поле ввода',width = 22)        #Кнопка очистки
but4.place(x = '1',y = '55')
but4.bind('<Button-1>',del1)

listbox = Listbox(root,width = 30,height = 10)       #Здесь выводим результат
listbox.place(x = '170',y = '90')

num1 = Button(root,text = '1',width = 2,height = 1,command=lambda:kn1(1))     #num1-num10 - Создаем кнопки для ввода
num1.place(x = '30',y = '240')


num2 = Button(root,text = '2',width = 2,height = 1,command=lambda:kn1(2))
num2.place(x = '60',y = '240')


num3 = Button(root,text = '3',width = 2,height = 1,command=lambda:kn1(3))
num3.place(x = '90',y = '240')


num4 = Button(root,text = '4',width = 2,height = 1,command=lambda:kn1(4))
num4.place(x = '30',y = '275')


num5 = Button(root,text = '5',width = 2,height = 1,command=lambda:kn1(5))
num5.place(x = '60',y = '275')


num6 = Button(root,text = '6',width = 2,height = 1,command=lambda:kn1(6))
num6.place(x = '90',y = '275')


num7 = Button(root,text = '7',width = 2,height = 1,command=lambda:kn1(7))
num7.place(x = '30',y = '310')


num8 = Button(root,text = '8',width = 2,height = 1,command=lambda:kn1(8))
num8.place(x = '60',y = '310')


num9 = Button(root,text = '9',width = 2,height = 1,command=lambda:kn1(9))
num9.place(x = '90',y = '310')


num0 = Button(root,text = '0',width = 2,height = 1,command=lambda:kn1(0))
num0.place(x = '60',y = '345')


numt = Button(root,text = '.',width = 2,height = 1,command=lambda:kn1('.'))
numt.place(x = '90',y = '345')

root.mainloop()
