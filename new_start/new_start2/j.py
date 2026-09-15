import json
while True:
    user_book_name = input("Book name:")
    user_book_author = input("Book author:")
    user_book_year = input("Book year:")
    data = {"name": user_book_name, "book_author": user_book_author,
            "book_year": user_book_year}
    with open("new_start/books.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    print(file)
