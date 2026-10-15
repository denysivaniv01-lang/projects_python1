import pandas as pd
import numpy as np
marks = np.random.default_rng()
col = []

for students in range(1, 102):
    students_mark = marks.integers(low=0, high=101, size=2)
    average = students_mark.mean()
    col.append({
        "Ім'я": "Anton",
        "Вік": 16,
        "оцінка з математики": students_mark[0],
        "оцінка з Програмування": students_mark[1],
        "Середній бал": average
    })

dt = pd.DataFrame(col)
print(dt.to_string())
students_eighty = dt[dt["Середній бал"] > 80]
print(f"Cтуденти у яких середній бал: >80:\n{students_eighty}")
