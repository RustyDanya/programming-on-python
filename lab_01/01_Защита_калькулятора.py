from tkinter import *
from math import sqrt

def main():

    global root
    root = Tk()
    root.title('Calculator')
    root.geometry('427x400')
    root.configure(bg = '#C0C0C0')
    root.bind('<Return>', solution)

    first_coefficient = Label(
        root, text = 'Введите коэффициент при x\u00b2',
        font = 'Arial 12', bg = '#C0C0C0')
    second_coefficient = Label(
        root, text = 'Введите коэффициент при x',
        font = 'Arial 12', bg = '#C0C0C0')
    third_coefficient = Label(
        root, text = 'Введите коэффициент при свободном члене',
        font = 'Arial 12', bg = '#C0C0C0')

    global label_warning
    label_warning = Label(
        root, bg = '#C0C0C0', font = 'Arial 20', width = 25)

    global label_solution
    label_solution = Label(
        root, width = 25, font = 'Arial 20',
        height = 5)

    global first_entry
    global second_entry
    global third_entry
    first_entry = Entry(
        root, width = 3, bg = 'white', font = 'Arial 10')
    second_entry = Entry(
        root, width = 3, bg = 'white', font = 'Arial 10')
    third_entry = Entry(
        root, width = 3, bg = 'white', font = 'Arial 10')

    button_solution = Button(
        root, text = 'Решить', width = 10)
    button_solution.bind('<Button-1>', solution)
    
    first_coefficient.place(x = 10, y = 50)
    second_coefficient.place(x = 10, y = 85)
    third_coefficient.place(x = 10, y = 120)
    first_entry.place(x = 375, y = 50)
    second_entry.place(x = 375, y = 85)
    third_entry.place(x = 375, y = 120)
    button_solution.place(x = 175, y = 160)
    label_warning.place(x = 10, y = 200)
    label_solution.place(x = 10, y = 210)
    root.mainloop()


def arg_solution():
    solution(None)


def solution(Event):
    a = first_entry.get()
    b = second_entry.get()
    c = third_entry.get()
    if len(a) > 0 and len(b) > 0 and len(c) > 0:
        label_warning.configure(text='')
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except:
            label_warning.configure(text = 'Некорректные значение', fg = 'Red')
            label_solution.configure(text = '')
            return
        if a == 0:
            if b == 0:
                if c == 0:
                    label_solution.configure(text = 'Любой x')
                else:
                    label_solution.configure(text = 'Нет решений')
            else:
                x = -c / b
                answer = 'X = ' + str('{:5.4f}'.format(x))
                label_solution.configure(text = answer)
        elif a != 0:
            D = pow(b, 2) - 4*a*c
            if D > 0:
                x1 = (-b + sqrt(D)) / (2*a)
                x2 = (-b - sqrt(D)) / (2*a)
                answer = 'X\u2081 = ' + str('{:5.4f}'.format(x1) + '\n X\u2082 = ' + str('{:5.4f}'.format(x2)))
                label_solution.configure(text = answer)
            elif D == 0:
                x = -b / (2*a)
                answer = 'Дискриминант равен 0.' + '\n Корень кратности 2' + '\n X = ' + str('{:5.4f}'.format(x))
                label_solution.configure(text = answer)
            else:
                answer = 'Действительных корней нет'
                label_solution.configure(text = answer)

if __name__ == '__main__':
    main()
