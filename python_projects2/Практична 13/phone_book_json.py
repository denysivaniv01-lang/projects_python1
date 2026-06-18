import json

FILE = "phone_book.json"

def read():
    with open(FILE, encoding="utf-8") as f:
        return json.load(f)

def save(contacts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

def show(contacts):
    for c in contacts:
        print(f"  {c['name']} — {c['phone']}, місто: {c['city']}")

# 1. Створити книгу
def create():
    save([
        {"name": "Анна",    "phone": "+380501112233", "city": "Львів"},
        {"name": "Богдан",  "phone": "+380672223344", "city": "Київ"},
        {"name": "Дарина",  "phone": "+380933334455", "city": "Одеса"},
    ])
    print("Телефонну книгу створено.")

# 2. Показати всі контакти
def show_all():
    show(read())

# 3. Додати контакт
def add():
    name  = input("Ім'я: ").strip()
    phone = input("Телефон: ").strip()
    city  = input("Місто: ").strip()

    if not name or not phone:
        print("Помилка: ім'я та телефон не можуть бути порожніми.")
        return

    contacts = read()
    contacts.append({"name": name, "phone": phone, "city": city})
    save(contacts)
    print(f"'{name}' додано.")

# 4. Знайти контакт
def find():
    name = input("Ім'я для пошуку: ").strip()
    for c in read():
        if c["name"] == name:
            show([c])
            return
    print("Контакт не знайдено.")

# 5. Оновити номер
def update():
    name  = input("Ім'я: ").strip()
    phone = input("Новий номер: ").strip()
    data  = read()

    for c in data:
        if c["name"] == name:
            c["phone"] = phone
            save(data)
            print("Номер оновлено.")
            return
    print("Контакт не знайдено.")

# 6. Видалити контакт
def delete():
    name     = input("Ім'я: ").strip()
    data     = read()
    filtered = [c for c in data if c["name"] != name]

    if len(filtered) == len(data):
        print("Контакт не знайдено.")
    else:
        save(filtered)
        print(f"'{name}' видалено.")


MENU = [
    ("Створити телефонну книгу",   create),
    ("Показати всі контакти",      show_all),
    ("Додати контакт",             add),
    ("Знайти контакт за іменем",   find),
    ("Оновити номер телефону",     update),
    ("Видалити контакт",           delete),
    ("Вийти",                      None),
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

# JSON (JavaScript Object Notation) — текстовий формат для зберігання
# структурованих даних. Від звичайного тексту відрізняється тим, що має
# чітку структуру (ключ: значення, списки, вкладеність), яку будь-яка
# програма може прочитати однаково. Наприклад:
#   [{"name": "Анна", "phone": "+380501112233", "city": "Львів"}]
#
# json.dump(data, f)  — перетворює Python-об'єкт (список/словник) у JSON
#                       і ЗАПИСУЄ його у файл f.
# json.load(f)        — ЧИТАЄ JSON з файлу f і повертає Python-об'єкт.
#
# ensure_ascii=False  — дозволяє зберігати кирилицю як є ("Анна"),
#                       без цього вона перетвориться на \u0410\u043d\u043d\u0430.
# indent=4            — форматує JSON з відступами (4 пробіли), щоб файл
#                       був читабельним для людини, а не одним суцільним рядком.

#   JSON-файл — це просто текст. Не можна "виправити один рядок" всередині
#   нього напряму, як у базі даних. Тому ми завантажуємо весь вміст у
#   Python-список, змінюємо його засобами Python (циклами, фільтрами),
#   а потім записуємо оновлений список назад у файл повністю.