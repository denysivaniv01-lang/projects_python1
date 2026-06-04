def Cel_Fah():
    c = print(f"{temp},75℃")
    return c


def Fah_Cel():
    f = print(f"75℃,{temp}")
    return f


user = input(
    "Як ви хочеие перевести операцію в Celsius у Fahrenheit чи навпаки?").capitalize()
temp = input("Введіть температуру!")

if user == "Felsius у fahrenheit":
    Cel_Fah()

elif user == "Fahrenheit у celsius":
    Fah_Cel()

else:
    print("Помилка")

# return потрібен для того щоб повертати результат з коробки функції в основний код
# return ми можем багато раз раз використовувати передає значення самій програмі а print тільки раз ввів і все більше використовувати не можна
# Це робить код чистим і зрозумілим якщо з'явитьсся помилка то ти будеш знати де це саме вона може сталасся