import math

def calculate_distance(x, y):
    return math.sqrt(x**2 + y**2)

def main():
    x1 = float(input("Введіть x1: "))
    y1 = float(input("Введіть y1: "))
    x2 = float(input("Введіть x2: "))
    y2 = float(input("Введіть y2: "))

    distance_A = calculate_distance(x1, y1)
    distance_B = calculate_distance(x2, y2)

    if distance_A < distance_B:
        print("Точка A ближче до початку координат.")
    elif distance_B < distance_A:
        print("Точка B ближче до початку координат.")
    else:
        print("Точки A і B однаково віддалені від початку координат.")

if __name__ == "__main__":
    main()
