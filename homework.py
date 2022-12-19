from math import sqrt

print("Введите коэффициенты для уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
dis = b**2 - 4 * a * c

if a == 0:
    print("Уравнение не является квадратным")
elif dis < 0:
    print("Нет решений")
elif dis == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    x1 = (-b + sqrt(dis)) / (2 * a)
    x2 = (-b - sqrt(dis)) / (2 * a)
    print(f"x1 = {x1}, x2 = {x2}")
