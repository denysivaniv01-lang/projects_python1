import json
while True:
    user_book_name = str(input("Book name:"))
    user_book_author = str(input("Book author:"))
    user_book_year = str(input("Book year:"))
    data ={"name":"Jong","book_author":"master","book_year":"123"}
    with open("books.json","w",encoding="utf-8") as file:
        json.dump(data)
