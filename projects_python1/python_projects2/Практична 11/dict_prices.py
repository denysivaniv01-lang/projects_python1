prices = {"banana": 50.00,
          "milk": 35.00,
          "apple": 10.00,
          "beer": 80.00,
          }
for товари, ціни in prices.items():
    print(товари, ціни,"грн")

print()
prices.update({"orange": 40.00})

print(f"Додавання ornge{prices}")

prices.pop("milk")
print(f"Видаляєм елемент milk{prices}")
print()

user = input("Введіть назву товару: ").lower()
if user in "banana":
    print(f"{user} {ціни}грн.")

else:
    print("товар не знайдено!")
print()

top_product = max(prices, key=prices.get)
print(f"Найдорожчий товар: {top_product} ціна: {ціни} грн.")

# Перевірка наявності ключа у словнику виконується за допомогою оператора 'in' (наприклад, user in prices), який повертає True, якщо такий ключ існує.
