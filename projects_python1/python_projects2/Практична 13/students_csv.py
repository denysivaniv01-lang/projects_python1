import csv

FILE = "students.csv"
FIELDS = ["name", "age", "grade"]

def read():
    with open(FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save(students):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(students)

def show(students):
    for s in students:
        print(f"  {s['name']} — {s['age']} років, оцінка: {s['grade']}")

# 1. Створити файл
def create():
    save([
        {"name": "Анна",   "age": "16", "grade": "10"},
        {"name": "Богдан", "age": "17", "grade": "11"},
        {"name": "Дарина", "age": "15", "grade": "9"},
        {"name": "Євген",  "age": "18", "grade": "12"},
    ])
    print("Файл створено.")

# 2. Показати всіх
def show_all():
    show(read())

# 3. Додати студента
def add():
    name  = input("Ім'я: ").strip()
    age   = input("Вік: ").strip()
    grade = input("Оцінка (1-12): ").strip()

    if not name or not grade.isdigit() or not (1 <= int(grade) <= 12):
        print("Помилка: ім'я не може бути порожнім, оцінка — від 1 до 12.")
        return

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow({"name": name, "age": age, "grade": grade})
    print(f"'{name}' додано.")

# 4. Оновити оцінку
def update():
    name  = input("Ім'я: ").strip()
    grade = input("Нова оцінка (1-12): ").strip()
    data  = read()

    for s in data:
        if s["name"] == name:
            s["grade"] = grade
            save(data)
            print("Оцінку оновлено.")
            return
    print("Студента не знайдено.")

# 5. Видалити студента
def delete():
    name    = input("Ім'я: ").strip()
    data    = read()
    filtered = [s for s in data if s["name"] != name]

    if len(filtered) == len(data):
        print("Студента не знайдено.")
    else:
        save(filtered)
        print(f"'{name}' видалено.")

# 6. Оцінка 11 або 12
def high_grades():
    show([s for s in read() if int(s["grade"]) >= 11])


MENU = [
    ("Створити файл",                  create),
    ("Показати всіх студентів",        show_all),
    ("Додати студента",                add),
    ("Оновити оцінку",                 update),
    ("Видалити студента",              delete),
    ("Студенти з оцінкою вище 10",     high_grades),
    ("Вийти",                          None),
]

while True:
    print("\n--- МЕНЮ ---")
    for i, (label, _) in enumerate(MENU, 1):
        print(f"{i}. {label}")

    choice = input("Вибір: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(MENU)):
        print("Невірний вибір.")
        continue

    label, action = MENU[int(choice) - 1]
    if action is None:
        print("До побачення!")
        break

    action()

# CSV — текстовий формат де дані розділені комами: Анна,16,10
# csv.DictReader/DictWriter — читає/пише рядки як словники {'name': 'Анна', ...}
# csv.reader/writer      — читає/пише рядки як списки  ['Анна', '16', '10']
# newline=""— щоб csv сам керував кінцями рядків (без зайвих пустих рядків на Windows)