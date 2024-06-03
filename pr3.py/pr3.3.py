angle1 = float(input("Введіть перший кут трикутника: "))
angle2 = float(input("Введіть другий кут трикутника: "))

if angle1 + angle2 < 180:
    print("Такий трикутник існує.")
    if angle1 == 90 or angle2 == 90 or (180 - angle1 - angle2) == 90:
        print("Трикутник є прямокутним.")
    else:
        print("Трикутник не є прямокутним.")
else:
    print("Такий трикутник не існує.")
