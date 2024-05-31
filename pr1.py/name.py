1
print ("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

2
import math4
radius = float(input("Введіть радіус кола: "))
area = math.pi * (radius ** 2)
print(f"Площа кола з радіусом {radius} дорівнює {area:.2f}")

3
color_list = ["Red", "Green", "White", "Black"]
first_color = color_list[0]
last_color = color_list[-1]
print(f"Перший колір у списку: {first_color}")
print(f"Останній колір у списку: {last_color}")

4
n = int(input("Введіть ціле число: "))
n1 = n
n2 = int(f"{n}{n}")
n3 = int(f"{n}{n}{n}")
result = n1 + n2 + n3
print(f"Результат обчислення {n} + {n}{n} + {n}{n}{n} дорівнює {result}")

5
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]
for number in numbers:
    if number == 237:
        break
    elif number % 2 == 0:
        print(number)

6
def check_zero_one_sequence(s):
    zero_count = 0
    one_count = 0
    i = 0
    length = len(s)
    while i < length:
        if s[i] == '0':
            while i < length and s[i] == '0':
                zero_count += 1
                i += 1
            while i < length and s[i] == '1':
                one_count += 1
                i += 1
            if zero_count != one_count:
                return False
            zero_count = 0
            one_count = 0
        else:
            i += 1
    return True
sequence1 = "01010101"
sequence2 = "00011100011"
print(check_zero_one_sequence(sequence1))
print(check_zero_one_sequence(sequence2))

7
def print_even_numbers(n, m):
    for i in range(-n, n + 1, m):
        if i % 2 == 0:
            print(i)
n = int(input("Введіть значення n: "))
m = 5
print_even_numbers(n, m)

8
import math
def calculate_combinations(n, m):
    if m > n:
        return 0
    return math.factorial(n) // math.factorial(n - m)
n = 25
m = int(input("Введіть свій порядковий номер у журналі: "))
combinations = calculate_combinations(n, m)
print(f"Кількість можливих комбінацій для {m} комірок: {combinations}")

9
my_list = [1, 2, 3, 4, 5]
L = [3, 6, 7]
my_list.extend(L)
print(my_list)
my_list.insert(1, 33333)
print(my_list)
my_list.reverse()
print(my_list)
my_list.append(3)
print(my_list)
my_list.remove(3)
print(my_list)
my_list.sort()
print(my_list)
my_list.clear()
print(my_list)

10
class LibraryAccount:
    def __init__(self, ID, last_name, first_name, group, course):
        self.ID = ID
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.course = course
        self.borrowed_books = []
        self.returned_books = []

    def display_info(self):
        print("ID:", self.ID)
        print("Прізвище:", self.last_name)
        print("Ім’я:", self.first_name)
        print("Група:", self.group)
        print("Курс:", self.course)
        print("Книги у боргу:", self.borrowed_books)
        print("Статистика книг:", self.returned_books)

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print("Книга '{}' додана у борг".format(book))

    def return_book(self, book):
        if book not in self.borrowed_books:
            print("Книга '{}' відсутня у списку боргу".format(book))
        else:
            self.borrowed_books.remove(book)
            self.returned_books.append(book)
            print("Книга '{}' повернута".format(book))

reader = LibraryAccount(1, "Білан", "Юля", "Група ІПЗс", 2)
while True:
    print("\nМеню:")
    print("1. Карта читача")
    print("2. Взяти книгу у борг")
    print("3. Повернути книгу")
    print("0. Вихід")

    choice = input("Введіть номер опції: ")
    if choice == "1":
        reader.display_info()
    elif choice == "2":
        book = input("Введіть назву книги: ")
        reader.borrow_book(book)
    elif choice == "3":
        if len(reader.borrowed_books) == 0:
            print("У вас немає книг у боргу")
        else:
            print("Книги у боргу:", reader.borrowed_books)
            book = input("Введіть назву книги, яку бажаєте повернути: ")
            reader.return_book(book)
    elif choice == "0":
        print("Дякую за користування програмою!")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")