
num = []

def save(res):
    num.append(res)

def result():
    if len(num) <= 0:
        print("Історія операцій порожня")
    else:
        print("\n--- ІСТОРІЯ ОПЕРАЦІЙ ---")
        for zapys in num:
            print(zapys)

def add(a, b):
    nums = (a + b)
    return nums

def minus(a, b):
    nums = (a - b)
    return nums

def multiply(a, b):
    nums = (a * b)
    return nums

def divide(a, b):
    if b == 0:
        print("Помилка: ділити на нуль не можна")
        return False
    else:
        nums = (a / b)
        return nums

def checker():
    while True:
        print("\n\t-----МЕНЮ------")
        print("1. Додати")
        print("2. Відняти")
        print("3. Помножити")
        print("4. Поділити")
        print("5. Показати історію")
        print("6. Вийти")

        user = input("Виберіть дію: ")

        if user == "6":
            print("До побачення!")
            return False

        elif user == "5":
            result()

        # Якщо користувач вибрав математичну дію (від 1 до 4)
        elif user in ["1", "2", "3", "4"]:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))

            if user == "1":
                res = add(a, b)
                print(f"Результат: {res}")
                zapys = f"{a} + {b} = {res}"
                save(zapys)

            elif user == "2":
                res = minus(a, b)
                print(f"Результат: {res}")
                zapys = f"{a} - {b} = {res}"
                save(zapys)

            elif user == "3":
                res = multiply(a, b)
                print(f"Результат: {res}")
                zapys = f"{a} * {b} = {res}"
                save(zapys)

            elif user == "4":
                res = divide(a, b)
                # Якщо ділення успішне (не False), то виводимо і зберігаємо
                if res is not False:
                    print(f"Результат: {res}")
                    zapys = f"{a} / {b} = {res}"
                    save(zapys)
        else:
            print("Неправильний вибір спробуйте ще")


checker()
# Функція-валідатор — це функція, яка перевіряє правильність даних (наприклад, чи не дорівнює дільник нулю).
# Повернення True/False або значень допомагає головній програмі зрозуміти, чи успішно пройшла операція.
# Розбиття на малі функції (декомпозиція) допомагає не плутатися в коді: математика окремо, меню окремо, історія окремо.