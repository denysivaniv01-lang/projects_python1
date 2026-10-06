import matplotlib.pyplot as mt
students = ["Іван", "Петро", "Анна", "Марія", "Олег"]
grades = [10, 8, 12, 10, 11]
mt.plot(students,grades, marker=".",
        markersize="10",
        linestyle="dashed")
mt.title("Середні оцінки з програмування",fontsize=20,
         family="Arial",
         color="#738fba")
mt.xlabel("Cтуденти",fontsize=15,
         family="Arial",
         color="black")
mt.show()
