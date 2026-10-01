import numpy as np
for students in range(1, 101):
    students_subjects = np.array(["Математика", "Фізкультура", "Історія"])
    mark = np.random.default_rng()
    students_mark = mark.integers(low=0, high=100, size=3)
    avarage = students_mark.mean()
    print(f"#{students} предмет:{students_subjects[0]} оцінка:{students_mark[0]}"),
    print(f"предмет:{students_subjects[1]} оцінка:{students_mark[1]}")
    print(f"предмет:{students_subjects[2]} оцінка:{students_mark[2]}")
    print(f"середній бал учня:{avarage:.2f}\n")
