import math

# --- 1. Параметри кола ---

r = float(input("Введіть радіус кола: "))

area = round(math.pi * r ** 2, 2)
circumference = round(2 * math.pi * r, 2)

print(f"Площа кола:    {area}")
print(f"Довжина кола:  {circumference}")


# --- 2. Тригонометрія ---

degrees = float(input("\nВведіть кут у градусах: "))
radians = math.radians(degrees)

print(f"sin({degrees}°) = {round(math.sin(radians), 4)}")
print(f"cos({degrees}°) = {round(math.cos(radians), 4)}")


# --- 3. Корінь та факторіал ---

n = int(input("\nВведіть ціле число: "))

print(f"√{n} = {round(math.sqrt(n), 4)}")
print(f"{n}! = {math.factorial(n)}")

# math.pi містить число π з точністю до 15 знаків після коми.
#   Якщо написати pi = 3.14 вручну — похибка накопичується з кожним
#   обчисленням. Для серйозних розрахунків це критично.
#   Те саме стосується всіх інших функцій модуля math — вони реалізовані
#   на рівні мови та дають максимально точний результат.
#
# math.sin() та math.cos() приймають кут у РАДІАНАХ, а не градусах.
#   Тому перед викликом потрібно конвертувати: math.radians(90) → 1.5707...
#   Без конвертації sin(90) поверне sin(90 радіан) — зовсім інше число.