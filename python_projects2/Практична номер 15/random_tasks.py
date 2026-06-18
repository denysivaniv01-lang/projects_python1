import random
import string


length = random.randint(8, 12)

chars = (
    string.ascii_lowercase +   # абвгд... abcde...
    string.ascii_uppercase +   # АБВГД... ABCDE...
    string.digits +            # 0123456789
    "!@#$%"                    # спецсимволи
)

password = "".join(random.choices(chars, k=length))
print(f"Згенерований пароль: {password}")


# --- 2. Гра "Вгадай число" ---

secret = random.randint(1, 100)
attempts = 0

print("\nЯ загадав число від 1 до 100. Спробуй вгадати!")

while True:
    guess = int(input("Твоя спроба: "))
    attempts += 1

    if guess < secret:
        print("Більше!")
    elif guess > secret:
        print("Менше!")
    else:
        print(f"Вітаю! Ви вгадали число за {attempts} спроби.")
        break


# Модуль random генерує псевдовипадкові числа — вони виглядають випадково,
#   але насправді обчислюються за математичним алгоритмом на основі "зерна"
#   (seed). Для більшості задач цього достатньо, але для криптографії — ні.
#
# random.randint(a, b) — повертає ціле число від a до b включно. Наприклад:
#   random.randint(1, 100) → будь-яке число від 1 до 100.
#
# random.choice(seq)   — повертає один випадковий елемент із послідовності.
#   random.choices(seq, k=n) — повертає список із n елементів (з повторами).