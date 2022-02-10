x = float(input())
y = float(input())
r = float(input())
if (y>=x+r and x**2+y**2<r**2) or (y<0 and x<0 and x**2+y**2<r**2):
    print("Попадает")
else:
    print("Не попадает")
