def determine_location(x, y):
    if x == 0 and y == 0:
        return "Точка знаходиться в початку координат."
    elif x == 0:
        return "Точка знаходиться на осі Y."
    elif y == 0:
        return "Точка знаходиться на осі X."
    elif x > 0 and y > 0:
        return "Точка знаходиться в першому координатному куті."
    elif x < 0 and y > 0:
        return "Точка знаходиться в другому координатному куті."
    elif x < 0 and y < 0:
        return "Точка знаходиться в третьому координатному куті."
    else:
        return "Точка знаходиться в четвертому координатному куті."

def main():
    x = float(input("Введіть x: "))
    y = float(input("Введіть y: "))
    
    result = determine_location(x, y)
    print(result)

if __name__ == "__main__":
    main()
