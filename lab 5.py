import math
from random import randint

def columnSum(mas):
    stringR = ""
    for j in range (len(mas)):
        sum = 0
        for i in range (len(mas)):
            if mas[i][j] > -1:
                sum += mas[i][j]
            else:
                sum = 0
                break
        if (sum>0):
            stringR = stringR + "Сумма "+ str(j+1) + " столбца = " + str(sum) + "\n" 
        else: 
            stringR =stringR + "В "+ str(j+1)+ " столбце есть отрицательное число" + "\n" 
    return stringR

def minSum(mas):
    minS = abs(mas[0][1]) + abs(mas[1][0])
    for j in range (1,len(mas)-1,1):
        jj=j
        newS = 0
        for i in range(0,jj+1,1):
            newS += abs(mas[i][j])
            j-=1
        j = jj
        if (newS < minS):
            minS=newS
        newS=0
        for i in range(len(mas)-1,jj-1,-1):
            newS += abs(mas[i][j])
            j+=1
        if (newS < minS):
            minS=newS
        j = jj
    print("Минимальная сумма = ", minS)     



n = int(input("Введите длину стороны матрицы:"))

mas = [[randint(-3, 9) for j in range(n)] for i in range(n)]
for i in range (n):
        print(mas[i])
print("")

#1) Подсчет суммы столбцах без отрицательных значений
print(columnSum(mas))

#2) Сумма модулей элементов параллельной и побочной диагоналей
minSum(mas)
input()    