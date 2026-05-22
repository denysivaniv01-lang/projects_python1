person = {"name": "Denis",
          "age": 16,
          "city": "Ivano-Frankivsk",
          "hobby": "Programming"}
print(person)
person.update({"email": "denys.v.ivaniv@ukd.edu.ua"})
print("="* 95)
print(f"Дадаєм в кінці @email {person}")
person.update({"age": 17})
print(f"Обновлення року{person}")
print("="* 95)
person.pop("hobby")
print(f"Видалення елемента hobby{person}")

print("="* 95)

print(f"виводим ключі{person.keys()}")
print(f"виводим значення{person.values()}")
# ключ це свого роду індекс по якому ми можем звертатисся напряму до його ім'я