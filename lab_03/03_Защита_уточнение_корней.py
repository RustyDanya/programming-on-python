from math import *

def func(x):
    return sin(x)

def proizv(x):
    return cos(x)

def method(a, b, eps, maxim):
    x0 = a
    x1 = b
    f0 = func(x0)
    f1 = func(x1)
    n = 0
    if f0*f1 > 0:
        return 'no', 0
    while n < maxim:
        x1 = x0 - (func(x0) / proizv(x0))
        if abs(x1 - x0) < eps:
            if x1 < a:
                return 'bot', 0
            if x1 > b:
                return 'top', 0    
            return x1, n
        n += 1
        x0 = x1
    return 'Iter', 0
    
def table(a, b, h, eps, maxim):
    i = a
    num = 1
    print('Коды ошибок:\n "0" - без ошибок \n "1" - Превысило допустимое'
          'количество итераций\n "2" - зашло за нижнюю границу\n "3" - '
          'зашло за верхнюю границу')
    print('N \t Интервал \t','{:8s}'.format('X'),'\t',
                      '{:8s}'.format('F(X)'), '\t Итерации','\t', 'Код ошибки')
    while i < b:
        if i+h <= b:
            x, n = method(i, i+h, eps, maxim)
        else:
            x, n = method(i, b, eps, maxim)
        i = round(i, 3)
        top = round(i+h,3)
        if x != 'no' and x != 'Iter' and x != 'bot' and x != 'top' and\
           (func(i) !=0 or i == a):
            print(num,'\t','{',i,';',top,'}\t','{:8.6f}'.format(x),
                  '\t','{:8.1e}'.format(func(x)),'\t','{:8}'.format(n),
                  '\t "0"')
            num += 1
        if x == 'Iter' or x == 'top' or x == 'bot':
            if func(i) * func(top) < 0 or func(top) == 0 or (func(i) !=0 or i == a):
                if x == 'Iter':
                    err = '"1"'
                elif x == 'bot':
                    err = '"2"'
                else:
                    err = '"3"'
                print(num,'\t','{',i,';',top,'}\t','{:8s}'.format('---'),'\t',
                      '{:8s}'.format('---'), '\t','{:8s}'.format('---'),'\t', err)
                num += 1
        i += h
a = float(input('Введите левую границу отрезка: '))
b = float(input('Введите правую границу отрезка: '))
h = float(input('Введите шаг: '))
eps = float(input('Введите точность: '))
maxim = int(input('Введите максимальное количество итераций: '))
table(a,b,h,eps,maxim)





