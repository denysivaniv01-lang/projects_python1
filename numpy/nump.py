import numpy as np
for students in range(1, 101):
    students_subjects = ([["Історія"],
                          ["Математика"],
                          ["Фізкультура"]])
    mark = np.random.uniform(low=1,high=101)

    print(f"#{students} предмет:{students_subjects} оцінка:{np.mean(mark)}"),
    # f"{students_subjects[1]} оцінка:{mark.uniform(1,101)}",
    # f"{students_subjects[2]} оцінка:{mark.mea(1,101)}")