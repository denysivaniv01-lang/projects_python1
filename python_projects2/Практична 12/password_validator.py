# Перевірка на довжину
def check_length(password):
    return len(password) >= 8

# Перевірка на цифру
def check_digit(password):
    for sym in password:
        if sym.isdigit():
            return True
    return False

# Перевірка на велику літеру
def check_upper(password):
    for sym in password:
        if sym.isupper():
            return True
    return False

def validate_password():
    password = input("Введіть пароль: ")

    if password == "":
        print("Пароль слабкий: порожній")
        return

    if not check_length(password):
        print("Пароль слабкий: занадто короткий")
        return

    if not check_digit(password):
        print("Пароль слабкий: не містить цифру")
        return

    if not check_upper(password):
        print("Пароль слабкий: не містить велику літеру")
        return

    # Якщо ми дійшли сюди, значить жоден return не спрацював
    print("Пароль надійний")

validate_password()

# 1. Функція-валідатор — перевіряє дані (пароль) на правильність.
# 2. True/False — зручні "прапорці": підходить умова чи ні.
# 3. Декомпозиція — ми розбили код на малі частини, щоб не заплутатися в логіці.