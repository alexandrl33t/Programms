import math
print("Введите x")
x=int(input())
if (x>=-4 and x<-2):
    print('y=',x+3)
elif (x>=-2 and x<4):
    print('y=',-(x/2))
elif (x>=-4) and (x<6):
    print('y=',-2)
if (x>10 or x<-4):
    print("Неверный x")
if(x>5):
    print("Введите R")
    r=int(input())
    func = r**2-(x-8)**2+2
if (x>=6) and (x<10) and (func > 0):
    print('y=', math.sqrt(func))