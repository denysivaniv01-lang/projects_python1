grades_list = []

def add_grade():
    user_input = input("Введіть оцінку (від 1 до 12): ")
    
    # Перевіряємо, чи користувач ввів саме число, а не літери
    if user_input.isdigit():
        grade = int(user_input)
        if 1 <= grade <= 12:
            grades_list.append(grade)
            print(f"Оцінку {grade} успішно додано!")
        else:
            print("Помилка: оцінка має бути в межах від 1 до 12!")
    else:
        print("Помилка: введіть ціле число!")


#CALLBACK-ФУНКЦІЇ ДЛЯ АНАЛІТИКИ
def show_grades(lst):
    print(f"Всі оцінки у списку: {lst}")

def show_average(lst):
    avg = sum(lst) / len(lst)
    print(f"Середній бал: {avg:.2f}")  # Округлюємо до 2 знаків після коми

def show_max(lst):
    print(f"Найвища оцінка: {max(lst)}")

def show_min(lst):
    print(f"Найнижча оцінка: {min(lst)}")

def show_count(lst):
    print(f"Загальна кількість оцінок: {len(lst)}")


# --- ГОЛОВНА ФУНКЦІЯ ОБРОБКИ (ПРИЙМАЄ CALLBACK) ---
def analyze(lst, callback_func):
    if len(lst) <= 0:
        print("Помилка: Оцінок немає! Спочатку додайте хоча б одну оцінку.")
        return
    
    # Якщо все добре — викликаємо callback-функцію, яку нам передали без дужок
    callback_func(lst)


#ГОЛОВНИЙ ЦИКЛ ПРОГРАМИ (МЕНЮ)
def main_menu():
    while True:
        print("\n\t--- МЕНЕДЖЕР ОЦІНОК ---")
        print("1. Додати оцінку")
        print("2. Показати всі оцінки")
        print("3. Показати середній бал")
        print("4. Показати найвищу оцінку")
        print("5. Показати найнижчу оцінку")
        print("6. Показати кількість оцінок")
        print("7. Вийти")

        user = input("Виберіть дію (1-7): ")

        if user == "1":
            add_grade()  # Тут просто додаємо, перевірка порожнечі не потрібна

        elif user == "2":
            analyze(grades_list, show_grades)

        elif user == "3":
            analyze(grades_list, show_average)

        elif user == "4":
            analyze(grades_list, show_max)

        elif user == "5":
            analyze(grades_list, show_min)

        elif user == "6":
            analyze(grades_list, show_count)

        elif user == "7":
            print("До побачення! Програму завершено.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз (1-7).")

main_menu()