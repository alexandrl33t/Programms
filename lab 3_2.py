import matplotlib.pyplot as plt
r = 1
def print_table(list):
    print("+{:_<47}+".format("_"))
    print("|{:^47}|".format("Таблица значений"))
    print("|{:-<47}|".format("-"))
    print("|{:^10}|{:^10}|{:^25}".format("X", "Y", "Результат"))
    for x, y, result in list:
        print("|{:-<47}|".format("-"))
        print("|{:^10}|{:^10}|{:^25}|".format(x, y, result))
    print("+{:-<47}+".format("-"))

goals = list()
for k in range (0,10):
    x = float(input("Ведите координаты X: "))
    y = float(input("Введите координаты Y: "))

    result = ''
    if (y>=x+r and x**2+y**2<r**2) or (y<0 and x<0 and x**2+y**2<r**2):
        print("Попадает")
        result = "Попал" 
    else:
        print("Не попадает")
        result = "Промах"
    goals.append((x,y,result))
    plt.plot(x, y, '.', color='red')

print_table(goals)
plt.show()
input();