<<<<<<< HEAD
email = "user@example.com"
search = email.find("@")  # шукає заданий символ і виводе де він знаходиться
print("знайдено @ в",search)

кількість = email.count("e")  # рахуйє скільки є таких самих букв
print("e знайдено",кількість)

if "user" and ".com" in email:
    print("Все добре")

else:
    print("Все погано")


user = input("Введіть рядок: ")
if user.isdigit():
    print("Ви ввчели число")
elif user.isalpha():
    print("Ви ввели Букви")
elif user.isalnum():
    print("В вашому тексті є цифри і букви")

else:
    print("Помилка можливо ви ввели пробіл або символ!")
=======
email = "user@example.com"
search = email.find("@")  # шукає заданий символ і виводе де він знаходиться
print("знайдено @ в",search)

кількість = email.count("e")  # рахуйє скільки є таких самих букв
print("e знайдено",кількість)

if "user" and ".com" in email:
    print("Все добре")

else:
    print("Все погано")


user = input("Введіть рядок: ")
if user.isdigit():
    print("Ви ввчели число")
elif user.isalpha():
    print("Ви ввели Букви")
elif user.isalnum():
    print("В вашому тексті є цифри і букви")

else:
    print("Помилка можливо ви ввели пробіл або символ!")
>>>>>>> b13a8fbef3ff269eace11adb4b8db262612244a7
