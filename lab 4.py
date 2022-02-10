import math
import random
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)


def my_round(a):
    k = a
    return round(k,2)

def print_mas(a):
    mas = ''
    for i in range(n):
        mas += str(my_round(a[i])) + ' '
    print(mas)

def max_arr(a):
    k = a[0]
    for i in range(1,len(a)):
        if a[i] > k:
            k = a[i]
    return k

def sum(a):
    k = []
    for i in range(len(a)-1, 0, -1):
        if (a[i]<= 0):
            k.append(a[i])
        else: 
            k.append(a[i])
            break
            
    return round(math.fsum(a) - math.fsum(k), 2)

def sort(arr, a, b):
    i=0
    while(i < len(arr)):
        if (a < abs(arr[i]) < b): 
            arr.pop(i)
            arr.append(0)
            i -=1
        else: 
            i +=1
    return arr


n= int(input("ВВедите кол-во элементов массива: "))

from random import triangular
mas = ''

arr=[triangular(-10,10, 2) for i in range(n)]

#функция вывода массива в строку
print_mas(arr)  
print("Отсортированный массив:")
print_mas(quicksort(arr))

print('')
# 1) округление + функция вывода макс элемнта     
print("MAX элемент массива: ", my_round(max_arr(arr)))

print('')
# 2) сумма элементов до последнего положительного
print("Сумма всех элементов до последнего положительного: ",sum(arr))

print('')
# 3) сжатие массива

a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))
print('')

print("Отсортированный массив с интервалом:")
print_mas(sort(arr, a, b))

input();