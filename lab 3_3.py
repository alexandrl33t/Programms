import math
import matplotlib.pyplot as plt

def print_table(list):
    print("+{:_<31}+".format("_"))
    print("|{:^31}|".format("Таблица значений"))
    print("|{:-<31}|".format("-"))
    print("|{:^15}|{:^15}|".format("X", "ln(1+x)/(1-x)"))
    for x, y in list:
        print("|{:-<31}|".format("-"))
        print("|{:^15.4f}|{:^15.8f}|".format(x, y))
    print("+{:-<31}+".format("-"))

def func(x, e):
    i = 0;
    res = 0
    k = 0.0
    while 1:
        k = round(res, e)
        res +=x**(2*i+1) / (2*i+1)
        i+=1
        if k == round(res, e):
            return 2* res
 

x1= float(input("Введите x нач: "))
x2= float(input("Введите x кон: "))
dx = float(input("Введите шаг dx: "))
e = int(input("Введите точность e: "))
plt.xlim(x1 - 0.125, x2 + 0.125)
if (abs(x1) < 1 and abs(x2) < 1 and 0<dx<2):
        l = list()
        x = x1
        while (x<x2):
            res = func(x, e)
            l.append((x, res))
            x+=dx
            plt.plot(x, res, '.', color='red')
        print_table(l)
        plt.show()


input()