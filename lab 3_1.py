import math
import sys
import matplotlib.pyplot as plt

x1=float(input("Введите x нач (x>-5): "))
x2=float(input("Введите x кон (x<11):"))
if (x1<-4 or x2 >10 or x1>x2):
    print("Неверные данные")
    sys.exit()
dx=float(input("Введите шаг dx: "))
plt.xlim(x1 - 0.125, x2 + 0.125)
isR = False
def print_table(list):
    print("+{:_<31}+".format("_"))
    print("|{:^31}|".format("Таблица значений"))
    print("|{:-<31}|".format("-"))
    print("|{:^15}|{:^15}|".format("X", "Y"))
    for x, y in list:
        print("|{:-<31}|".format("-"))
        print("|{:^15.4f}|{:^15.8f}|".format(x, y))
    print("+{:-<31}+".format("-"))


x = x1
l = list()
while (x <= x2+1):
    y = 0.0
    x = x1

    if (x>=-4 and x<-2):
        y= x+3
        l.append((x, y))
    elif (x>=-2 and x<4):
       y = -(x/2)
       l.append((x, y))
    elif (x>=4) and (x<6):
        y = -2
        l.append((x, y))
    elif (x>=6) and (x<10):
        func = math.sqrt(abs(4-(x-8)**2)) - 2
        y = round(func,1)
        l.append((x, y))
    plt.plot(x, y, '.', color='red')
    x1 +=dx

print_table(l)
plt.show()

input()    