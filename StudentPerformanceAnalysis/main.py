import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

res = pd.read_csv("КІПЗс-25-3_оцінки_готові.csv")
res.columns = res.columns.str.strip()

print(res.head(5))
print(f"кількість студентів та стовпців:{res.shape}")
print(f"Назви колонок:{res.columns.tolist()}")
print("-" * 30)

dates = ["09.09.2026", "12.09.2026", "25.09.2026", "02.10.2026", "09.10.2026"]

res = res.dropna(subset=["Студент"])
res["Студент"] = res["Студент"].astype(str).str.strip()
res = res[res["Студент"] != ""]

text_marks = ["н", "в", "Н", "В", "н.", "в."]

for col in dates:
    res[col] = res[col].astype(str).str.strip()
    res[col] = res[col].replace(text_marks, np.nan)
    res[col] = res[col].str.replace(",", ".", regex=False)
    res[col] = pd.to_numeric(res[col], errors="coerce")

g = res[dates].to_numpy(float)
grades_table = res[["Студент"] + dates]

res["Середній бал"] = np.nanmean(g, axis=1)
res["Оцінок 1-3"] = ((g >= 1) & (g <= 3)).sum(axis=1)
res["Статус"] = np.where(res["Середній бал"] < 7, "Потребує уваги", "Добре")
summary = res[["Студент", "Середній бал", "Оцінок 1-3", "Статус"]]

print(f"Кількість студентів після очищення: {len(res)}")
print(
    f"Середній групи: {np.nanmean(g):.2f}, Max: {np.nanmax(g)}, Min: {np.nanmin(g)}")
print(f"Студентів із середнім < 7: {(res['Середній бал'] < 7).sum()}")
print("\nПотребують уваги:")
print(summary[summary["Статус"] == "Потребує уваги"]
      [["Студент", "Середній бал"]])

a = res["Середній бал"].to_numpy()
d = np.nanmean(g, axis=0)

print(f"Дата з найнижчим середнім балом: {dates[np.nanargmin(d)]}")

plt.figure()
plt.bar(res["Студент"], a, color=np.where(a < 7, "red", "green"))
plt.xticks(rotation=90)
plt.xlabel("Студент")
plt.ylabel("Середній бал")
plt.title("Середній бал студентів")
plt.tight_layout()
plt.savefig("1.png")
plt.close()

plt.figure()
plt.plot(dates, d, marker="o")
plt.grid()
plt.xticks(rotation=45)
plt.xlabel("Дата")
plt.ylabel("Середній бал")
plt.title(f"Найнижча дата: {dates[np.nanargmin(d)]}")
plt.tight_layout()
plt.savefig("2.png")
plt.close()

plt.figure()
x = g[~np.isnan(g)]
plt.hist(x, bins=np.arange(.5, 13.5), alpha=.7, label="Всі оцінки")
plt.hist(x[(x >= 1) & (x <= 3)], bins=np.arange(.5, 4.5),
         color="red", alpha=.7, label="Оцінки 1-3")
plt.xlabel("Оцінка")
plt.ylabel("Кількість")
plt.title("Розподіл оцінок")
plt.legend()
plt.tight_layout()
plt.savefig("3.png")
plt.close()

data = list(zip(res["Студент"], res["Середній бал"]))
check = sorted(data, key=lambda x: x[1])

for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and data[j][1] > key[1]:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key

print("\n5 найнижчих результатів:")
for s in data[:5]:
    print(s)

print("Порівняння зі sorted():", data == check)

summary.to_csv("results.csv", index=False, encoding="utf-8-sig")
print("\nФайл results.csv успішно збережено!")
