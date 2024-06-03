import math

x1 = float(input("Введіть x1: "))
y1 = float(input("Введіть y1: "))
x2 = float(input("Введіть x2: "))
y2 = float(input("Введіть y2: "))

distance_A = math.sqrt(x1**2 + y1**2)
distance_B = math.sqrt(x2**2 + y2**2)

if distance_A < distance_B:
    print("Точка A ближче до початку координат.")
elif distance_B < distance_A:
    print("Точка B ближче до початку координат.")
else:
    print("Точки A і B однаково віддалені від початку координат.")
