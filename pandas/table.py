import pandas as pd
for students in range(0,101):
    for marks in range(0,101):
        series = pd.Series("Hi",index=["Ім'я","Вік","оцінка з математики","оцінка з Програмування"])
        print(f"#{students} {series}")