lis = []

def add_item(name, price):
    print(f"Додавання {name} та {price}грн до списку")
    lis.append((name,price))
def total_price():
    total = sum(price for name, price in lis)
    print("загальна сума разам{total}грн")
def show_items():
   if not lis:
      print("Ваш список пустий")
   else:
       for name,price in lis:
          print(f"Ваш список ім'я товару:{name} ціна товару:{price}")
while True:
   print("\nВиберіть дію яку ви хочете зробити?")
   print("1.Додати товар+ціну")
   print("2.Рахує загальну суму покупок")
   print("3.Виводить загальний список покупок та їх ціни")
   print("4.Вийти")
   user = int(input("Введіть число:"))
   if user == 1:
    towar_name = str(input("Введіть товар який ви хочете:")).capitalize()
    towar_price = int(input("Введіть ціну товару:"))
    add_item(towar_name, towar_price)

   elif user == 2:
    total_price()
   elif user == 3:
      show_items()
   elif user == 4:
      print("Ви вийшли з програми")
      break

    



