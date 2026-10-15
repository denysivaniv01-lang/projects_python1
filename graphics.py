import matplotlib.pyplot as mt
import numpy as np
students = np.array(["Іван", "Петро", "Анна", "Марія", "Олег"])
grades = np.array([10, 8, 12, 10, 11])
mt.plot(students, grades, marker=".",
        markersize="10",
        linestyle="dashed",
        color="red",
        label="Оцінки студентів")
mt.title("Середні оцінки з програмування", fontsize=20,
         family="Arial",
         color="#738fba")
mt.xlabel("Cтуденти", fontsize=15,
          family="Arial",
          color="black")
mt.ylabel("Оцінки", fontsize=15,
          family="Arial",
          color="black")
mt.grid(True)
mt.legend(loc="upper left")
mt.show()

# Стовпчикова діаграма
math_grades = np.array([6, 7, 12, 8, 10])
students = np.array(["Іван", "Петро", "Анна", "Марія", "Олег"])
colors = ("#58ccb1", "#00ff1e", "#d1f5a2", "#e3b6e1", "#3c1487")
mt.bar(students, math_grades, color=colors)
mt.title("Середні оцінки з Математики", fontsize=20,
         family="Arial",
         color="blue")
mt.xlabel("Cтуденти")
mt.ylabel("Оцінки")
mt.show()

# Кругова діаграма
subjects = ["Програмування","Математика","Англійська","Інші предмети"]
time = np.array([40, 30, 20, 10])
mt.pie(time, labels=categories,
       autopct="%1.1f%%")
mt.title("Час на підготовку")
mt.show()
