# Программа выполняет пирамидальную сортировку массива.
# Воробьев Даниил ИУ7-21Б

from tkinter import *
from math import sqrt
from random import *
from tkinter import messagebox
import timeit

pop = 0

# Функция для проверки вводимых данных
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def tablica(event):     # Главная функция
    a = enta.get()
    b = entb.get()
    c = entc.get()    
    if is_number(a) == False or is_number(b) == False or is_number(c) == False: # Вывод ошибок
        messagebox.showerror('Ошибка', 'Некорректный ввод')
    elif (a == b or b == c or a == c) :
        messagebox.showerror('Ошибка', 'Введите различные значения')
    elif (int(a) < 1 or int(b) < 1 or int(c) < 1):
        messagebox.showerror('Ошибка', 'Введите положительные значения')
        
    else:   # Создание рандомных масивов
        
        a = int(a)
        b = int(b)
        c = int(c)
        A = [0] * a
        B = [0] * b
        C = [0] * c
        for i in range(a):
            A[i] = randint(-10, 10)
        for i in range(b):
            B[i] = randint(-10, 10)
        for i in range(c):
            C[i] = randint(-10, 10)
            
        timeArand = sort(A)
        timeAup = sort(A)
        A.reverse()
        timeAdown = sort(A)

        timeBrand = sort(B)
        timeBup = sort(B)
        B.reverse()
        timeBdown = sort(B)

        timeCrand = sort(C)
        timeCup = sort(C)
        C.reverse()
        timeCdown = sort(C)

        upA.delete(0, END)
        upB.delete(0, END)
        upC.delete(0, END)
        randA.delete(0, END)
        randB.delete(0, END)
        randC.delete(0, END)
        downA.delete(0, END)
        downB.delete(0, END)
        downC.delete(0, END)

        upA.insert(END, '{:10.7f}'.format(timeAup))
        upB.insert(END, '{:10.7f}'.format(timeBup))
        upC.insert(END, '{:10.7f}'.format(timeCup))
        randA.insert(END, '{:10.7f}'.format(timeArand))
        randB.insert(END, '{:10.7f}'.format(timeBrand))
        randC.insert(END, '{:10.7f}'.format(timeCrand))
        downA.insert(END, '{:10.7f}'.format(timeAdown))
        downB.insert(END, '{:10.7f}'.format(timeBdown))
        downC.insert(END, '{:10.7f}'.format(timeCdown))

def heap_sort(array):   # Пирамидальная сортировка 

    def sift_down (parent, limit):
        item = array[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and array[child] < array[child + 1]:
                child += 1
            if item < array[child]:                                     
                array[parent] = array[child]
                parent = child
            else:
                break
        array[parent] = item
    # Тело функции heap_sort
    length = len(array)
    # Формирование первичной пирамиды
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        array[0], array[index] = array[index], array[0]
        sift_down(0, index)


def sort(array):    # Сортировки массивов трех различных размерностей
    
    x = timeit.default_timer()

    array = list(array)
    heap_sort(array)

    return timeit.default_timer() - x

def sort_mas(D):    #Сортировка введенного массива малой размерности

    D1 = []
    D = entd.get()
    for s in D.split():
        try:
            D1.append(int(s))
        except:
            messagebox.showerror('Ошибка', 'Некорректный ввод')
    D1 = list(D1)    
    heap_sort(D1)
    masd.delete(0, END)
    masd.insert(END, D1)
    
    
#  Конструирование графического интерфейса
root = Tk()
root.title('Пирамидальная сортировка')
root.geometry('740x250')


def menu1():                               #Основная функция сортировки
    tablica(root)

def menu2():                   #Выводим информацию об авторе и программе
    root2 = Tk()
    root2.geometry('300x80')
    lab1 = Label(root2,text='Воробьев Даниил.\n ИУ7-21Б \n Пирамидальная сортировка массива.',
                  font='Arial 12')                             
    lab1.place(x=5, y=10)

m = Menu(root)                          #Создаем падающее меню
root.config(menu = m)
fm = Menu(m)
m.add_cascade(label = 'Меню',menu = fm)
fm.add_command(label = 'Выполнить сортировку',command = menu1)    
fm.add_command(label = 'О программе',command = menu2)

                                        # Создание кнопок и окон
enta = Entry(root,
             width=7, bg='#e6e6e6'
             , font='Arial 12', bd=3)
enta.pack()

entb = Entry(root,
             width=7, bg='#e6e6e6'
             , font='Arial 12', bd=3)
entb.pack()

entc = Entry(root,
             width=7, bg='#e6e6e6'
             , font='Arial 12', bd=3)
entc.pack()

entd = Entry(root,
             width=30, bg='#e6e6e6'
             , font='Arial 12', bd=3)
entd.pack()

lena = Label(root,
             text='Длина первого массива =',
             font='Arial 8', bd=3)
lenb = Label(root,
             text='Длина второго массива =',
             font='Arial 8', bd=3)
lenc = Label(root,
             text='Длина третьего массива =',
             font='Arial 8', bd=3)

button1_sort = Button(root,
                     text='Выполнить сортировку', font='SegoePrint 9',
                     width=20, bd=3)

button2_sort = Button(root,
                     text='Sort', font='SegoePrint 9',
                     width=20, bd=3)

Amark = Label(root,
              text='1',
              font='Arial 10', bd=3)
Bmark = Label(root,
              text='2',
              font='Arial 10', bd=3)
Cmark = Label(root,
              text='3',
              font='Arial 10', bd=3)
upmark = Label(root,
               text='sort',
               font='Arial 10', bd=3)
randmark = Label(root,
                 text='random',
                 font='Arial 10', bd=3)
downmark = Label(root,
                 text='reverse',
                 font='Arial 10', bd=3)

upA = Listbox(root,
              width=13, height=1,
              bg='#e6e6e6')
randA = Listbox(root,
                width=13, height=1,
                bg='#e6e6e6')
downA = Listbox(root,
                width=13, height=1,
                bg='#e6e6e6')
upB = Listbox(root,
              width=13, height=1,
              bg='#e6e6e6')
randB = Listbox(root,
                width=13, height=1,
                bg='#e6e6e6')
downB = Listbox(root,
                width=13, height=1,
                bg='#e6e6e6')
upC = Listbox(root,
              width=13, height=1,
              bg='#e6e6e6')
randC = Listbox(root,
                width=13, height=1,
                bg='#e6e6e6')
downC = Listbox(root,
                width=13, height=1,
                bg='#e6e6e6')
masd = Listbox(root,
                width=38, height=1,
                bg='#e6e6e6')

button1_sort.bind('<Button-1>', tablica)
root.bind('<Return>', tablica)

button2_sort.bind('<Button-1>', sort_mas)
root.bind('<Return>', sort_mas)

lena.place(x=20, y=11)
enta.place(x=170, y=10)
lenb.place(x=250, y=11)
entb.place(x=400, y=10)
lenc.place(x=480, y=11)
entc.place(x=630, y=10)

entd.place(x=20, y=200)

Amark.place(x=131, y=50)
Bmark.place(x=232, y=50)
Cmark.place(x=333, y=50)

upmark.place(x=25, y=70)
randmark.place(x=25, y=110)
downmark.place(x=25, y=150)

upA.place(x=100, y=72)
upB.place(x=200, y=72)
upC.place(x=300, y=72)
randA.place(x=100, y=112)
randB.place(x=200, y=112)
randC.place(x=300, y=112)
downA.place(x=100, y=152)
downB.place(x=200, y=152)
downC.place(x=300, y=152)

masd.place(x=310 , y=200)

button1_sort.place(x=488, y=100)
button2_sort.place(x=550, y=200)

root.mainloop()

