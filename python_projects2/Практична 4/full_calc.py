first_num = float(input("Введіть_число: "))  # Беремо перше число
Two_num = float(input("Введіть_число: "))   # Беремо друге число


res_plus = first_num + Two_num # Просто додаємо
res_minus = first_num - Two_num # Віднімаємо
res_множення = first_num * Two_num # Множимо
res_ділення = first_num / Two_num # Звичайне ділення (як на калькуляторі)
res_цілочисле = first_num // Two_num # Ділимо і відкидаємо «хвіст» (тільки ціле число)
res_остача = first_num % Two_num # Дізнаємося, скільки залишилося після ділення
res_степінь = first_num ** Two_num # Зводимо перше число у степінь другого

print("\n")
print("Основі операції")  # Показуємо результати на екрані

# виводимо приклади
print(f"{first_num} + {Two_num} = {res_plus}")
print(f"{first_num} - {Two_num} = {res_minus}")
print(f"{first_num} * {Two_num} = {res_множення}")
print(f"{first_num} ** {Two_num} = {res_степінь}")

# Порівнюємо різні типи ділення, щоб побачити різницю
print("\n", "=" * 20)
print("ПОРІВНЯННЯ ТРЬОХ ВИДІВ ДІЛЕННЯ")

print(res_ділення)  # Покаже результат з комою
print(res_цілочисле)  # Покаже тільки цілу частину
print(res_остача)  # Покаже тільки те, що не поділилося порівну

print("=" * 20)  # Малюємо ще одну лінію в кінці
