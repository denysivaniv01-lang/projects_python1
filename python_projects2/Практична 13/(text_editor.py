while True:
    print("1.Показати всі завдання.")
    print("2.Додати завдання.")
    print("3.Редагувати завдання")
    print("4.Видалити завдання")
    print("5.Очистити файл")
    print("6.Вийти")
    
    user = int(input("Введіть число якесь: "))
if user == 1:
    print("Ось ваш список")
    with open("tasks.txt", "r", encoding="utf-8") as file:
        line1 = file.readline()
    if not tasks:
            print("Список завдань порожній!")
    else:
         num = 1
         for li in line1:
              print(li)