
def pop():
    print("Hi")
    print("Hi")
    print("Hi")


def sum_numbers(a, b):
    result = a + b
    return result  # Повертаємо значення назовні

# Тепер ми можемо записати цей результат у змінну
total = sum_numbers(5, 10)
print(total)  # Виведе 15

pop()

print(total)  # Виведе 15