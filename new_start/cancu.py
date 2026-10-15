try:
    user_input = int(input("Введіть число 1: "))
    user_input2 = int(input("Введіть число 2: "))
    choice = str(input("Виберіть одну з варіантів +, -, *, /: "))

    def choice_new(var):
        if var == "+":
            res = user_input + user_input2
            print(f"Ваш резульатат(+): {res}")
        elif var == "-":
            res = user_input - user_input2
            print(f"Ваш резульатат(-): {res}")

        elif var == "*":
            res = user_input * user_input2
            print(f"Ваш резульатат(*): {res}")

        elif var == "/":
            res = user_input / user_input2
            print(f"Ваш резульатат(/): {res}")
        else:
            print("помилка: вам потрібно було вибрати одне з начень +, -, *, /")
    choice_new(choice)
    
except ValueError:
    print("ви написали число буквами а потрібно числом!")
except ZeroDivisionError:
    print("На нуль ділити не можна!")
