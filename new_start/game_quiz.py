import random
pc = random.randint(1, 100)
while True:
    user_input = int(input("Введіть число: "))
    if user_input == pc:
        print(f"Молодці ви вгaдали це:{pc}")
        break
    elif user_input >= pc:
        print("завилике число")
    elif user_input <= pc:
        print("замале число")