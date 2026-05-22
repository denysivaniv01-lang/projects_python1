prices = {"banana": 50.00,
          "milk":35.00,
          "apple": 10.00,
          "beer":80.00,
          }
for товари,ціни in prices.items():
    print(товари,ціни,end ="грн. ")

print()
prices.update({"orange":40})

print(f"Додавання ornge{prices}")

prices.pop("milk")
print(f"Видаляєм елемент milk{prices}")

user = input("Введіть назву товару: ")
if user in "banana":
    print(f"{user} {ціни}грн.")

else:
    print("що товар не знайдено")

