point = (10, 20, 30)
x, y, z = point

for el in (x, y, z):
    print(el)

point[1] = 25
print(point)
# Помилка TypeError виникає тому, що кортежі є незмінними (immutable)
# Незмінність означає,що видаляти або змінювати його елементи не можгна.