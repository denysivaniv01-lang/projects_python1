import json


def del_book():
    user_delete = input("Випишіть яку книгу ви хочете видалити?: ").strip()
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)

    for book in books:
        if book["name"] == user_delete:
            book["name"] = ""

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file)


while True:
    print("1. Додати нову книгу")
    print("2. Видалити книгу")
    print("3. Показати всі книги")
    print("4. Вийти")

    user = int(input("Введіть число: "))

    if user == 1:
        user_book_name = input("Book name: ")
        user_book_author = input("Book author: ")
        user_book_year = input("Book year: ")

        data = {"name": user_book_name,
                "author": user_book_author, "year": user_book_year}

        try:
            with open("books.json", "r", encoding="utf-8") as file:
                books = json.load(file)
        except:
            books = []

        if not books:
            print("oй а в file пусто")

        books.append(data)

        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(books, file)

    elif user == 2:
        del_book()

    elif user == 3:
        try:
            with open("books.json", "r", encoding="utf-8") as file:
                books = json.load(file)
                for book in books:
                    print(f"Назва: {book['name']}, Автор: {book['author']}, Рік: {book['year']}")
        except:
            print("Книг ще немає.")

    elif user == 4:
        break
