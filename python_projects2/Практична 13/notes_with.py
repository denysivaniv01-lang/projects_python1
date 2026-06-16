import datetime
now = datetime.datetime.now()
now = now.strftime("%d-%m-%y %H:%M:%S")

while True:
    print("1.Додати нонатку")
    print("2.Показати всі нонатки")
    print("3.Поувзвти нонатку по рядках")
    print("4.Вийти")
    user_choose = int(input("Введіть що ви хочете зробити"))

    if user_choose == 1:
        user = input("напишіть текст: ")
        with open("notes.txt", "a", encoding="utf-8") as files:
            res = files.write(now + user)
            res = files.write("\n")

    elif user_choose == 2:
        with open("notes.txt", "r", encoding="utf-8") as files:
            red = files.read()
        print(f"Вийде {red}")

        if len(user)==0:
            print("У вас немає нонаток!\n")
        else:
            print("У вас є нонаткі")

    elif user_choose == 3:
        with open("notes.txt", "r", encoding="utf-8") as files:
            i = 1
            for line in files:
                print(int(i),line)
                i += 1
    elif user_choose == 4:
        print("До побачення!")
        break            

# це конструкція з допомомогою якої ми маєм здатність відкриват та зразу закривати автоматично після заверешення роботи з файлом
# тому що це по перше не треба переживати про те що ти не створив закривач файл по друге це економить рядки коду.
# "a" - в нас додає до нашого списка нову інформацію не видаляючи стару. "w"-повністб очистує інформацію яка була записано і записує нову
# "read()"- виводить все зразу в свою ж чергу "for"-по кусках з відступами