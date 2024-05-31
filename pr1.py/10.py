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