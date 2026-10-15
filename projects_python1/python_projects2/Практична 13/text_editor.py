while True:
    print("\n1.Показати всі завдання.")
    print("2.Додати завдання.")
    print("3.Редагувати завдання")
    print("4.Видалити завдання")
    print("5.Очистити файл")
    print("6.Вийти")

    user = int(input("Введіть число якесь: "))

    if user == 1:
        print("Ось ваш список\n")
        with open("tasks.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()  # Зчитуємо всі рядки в список

            if len(lines) == 0:  # Якщо довжина списку нуль
                print("Список завдань порожній!")
            else:
                num = 1
                for line in lines:
                    print(num, line.strip())
                    num += 1

    elif user == 2:
        print("Додавання завдання\n")
        user_input = input("Введіть завдання: ")
        with open("tasks.txt", "a", encoding="utf-8") as file:
            file.write(user_input + "\n")
        print("Завдання додано!")

    elif user == 3:
        print("Редагувати завдання\n")
        user_change = int(input("Яке завдання ви хочете змінити? (номер): "))
        user_new = input("Запишіть зміну: ")

        with open("tasks.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Відкриваємо файл у режимі "w", щоб переписати його з новими даними
        with open("tasks.txt", "w", encoding="utf-8") as file:
            num = 1
            for line in lines:
                if num == user_change:
                    file.write(user_new + "\n")
                else:
                    file.write(line)  # Інакше записуємо старе завдання назад
                num += 1
        print("Завдання змінено!")

    elif user == 4:
        print("Видалити завдання\n")
        user_delete = int(input("Яке завдання ви хочете видалити? (номер): "))

        with open("tasks.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open("tasks.txt", "w", encoding="utf-8") as file:
            num = 1
            for line in lines:
                if num == user_delete:
                    pass
                else:
                    file.write(line)
                num += 1
        print("Завдання видалено!")

    elif user == 5:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            pass
        print("Файл повністю очищено!")

    elif user == 6:
        print("До побачення!")
        break

# компютер не може лізти ось так зразу та йому треба нагадувати тому ми копіюєм це у пам'ять(список)
# Він читає весь файл і розрізає його на список окремих рядків
# Він робить протилежне — бере список рядків і записує їх усі разом назад у файл одним махом.
# те що ми видаяєм лише маленькій кусочок а все решту лишаєтьсся нормально в свою чергу повне переписання стирає все що в нас є ф файлі