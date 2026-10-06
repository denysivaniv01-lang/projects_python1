def Cel_Fah(temp):
    c = (temp * 9/5) + 32
    return c


def Fah_Cel(temp):
    f = (temp - 32) * 5/9 
    return f



user = input("Як ви хочеие перевести операцію в Celsius у Fahrenheit чи навпаки?")
temp = input("Введіть температуру!")

temp_num = float(temp)

if "celsius" in user.lower():
    result = Cel_Fah(temp_num)
    print(f"{temp_num}°C = {result}°F")

elif "fahrenheit" in user.lower():
    result = Fah_Cel(temp_num)
    print(f"{temp_num}°F = {result}°C")

else:
    print("Помилка")

# return потрібен для того щоб повертати результат з коробки функції в основний код
# return ми можем багато раз раз використовувати передає значення самій програмі а print тільки раз ввів і все більше використовувати не можна
# Це робить код чистим і зрозумілим якщо з'явиться помилка то ти будеш знати де це саме вона може статисся