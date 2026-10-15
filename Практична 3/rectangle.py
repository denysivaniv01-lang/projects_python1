width = 12  # Ширина прямокутника
height = 5  # Висота прямокутника
area = width * height  # множим 12 * 5 = 60
perimeter = 2 * (width + height)  # 12 + 5 *2 = 34


# виводим наші ширину 60 та переметр 34
print(str(area) + "см", (str(perimeter)) + "см²")
# теж саме але для результату
print(f"результат= ", (area), (perimeter), sep=",")
