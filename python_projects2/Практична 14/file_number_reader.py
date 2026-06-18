try:
    with open("number.txt", "r", encoding="utf-8") as f:
        number = int(f.read().strip())

    print(f"Число: {number}")
    print(f"Множення на 2: {number * 2}")
    print(f"100 / {number} = {100 / number}")

except FileNotFoundError:
    print("Помилка: файл number.txt не знайдено.")

except ValueError:
    print("Помилка: у файлі має бути записане число.")

except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна.")

finally:
    print("Роботу з файлом завершено.")

# FileNotFoundError — виникає коли Python не може знайти файл за вказаним
#   шляхом. Причини: файл видалили, перейменували, або просто помилка в назві.
#
# Дані з файлу завжди читаються як рядок (str) — файл не знає, що там число.
#   Тому потрібна конвертація: int("25") → 25. Якщо там "hello" — ValueError.
#
# with open() — зручний спосіб відкрити файл: він сам закриє його після блоку,
#   навіть якщо всередині виникне помилка. Не потрібно писати f.close() вручну.