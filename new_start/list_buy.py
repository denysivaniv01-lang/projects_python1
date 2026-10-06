user_list = []
is_running = True
while is_running:
    print("Доступні параметри для списку покупок")
    print("Додати")
    print("Видалити")
    print("Показати")
    print("Вийти")

    user_choice = str(input("виберіть варіант: ")).capitalize()
    if user_choice == "Додати":
        user_word = input("Впишіть що ви хочете додати в список: ")
        user_list.append(user_word)

    elif user_choice == "Видалити":
        user_del = input("випішіть слово для видалення самого слова: ")
        if user_del in user_list:
            user_list.remove()

    elif user_choice == "Показати":
        print(user_list)
    elif user_choice == "Вийти":
        break

print(f"Ось ваш список покупок: {user_list}")
