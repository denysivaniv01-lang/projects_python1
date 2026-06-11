import datetime
while True:
    # 1 = print("Додати нонатку")
    # 2= print("Показати всі нонатки")
    # 3 = print("Поувзвти нонатку по рядках")
    # 4 = print("Вийти")
    user = input("напишіть текст")
    with open("notes.txt", "a", encoding="utf-8") as files:
        res = files.write(user+"\n")

        
print(dir(datetime()))