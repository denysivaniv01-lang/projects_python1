<<<<<<< HEAD
lis = [1, 10, 3, 7, 4]
print(f"індекс елемента 3: {lis.index(3)}")
print(f"сортування списку від найбільшого до найменшого")
lis.sort(reverse=True)
print(lis)
lis2_eror = [42,67,90]
lis2_normal = lis2_eror
lis2_normal.append(101)
print(lis2_eror)
print(lis2_normal)#Виводить [42, 67, 90, 101], тому що lis2_normal і lis2_eror це посилання на один і той же список який є в пам'яті і він діє на них обох однаково.
print("\n")
print(f"Копіювання списку за допомогою методу copy()")
lis3 = [42,67,90]
lis3_ok = lis3.copy()
lis3_new = lis3.copy()
lis3_new.append(101)
print(f"lis3: {lis3}")#оргнінальний список
=======
lis = [1, 10, 3, 7, 4]
print(f"індекс елемента 3: {lis.index(3)}")
print(f"сортування списку від найбільшого до найменшого")
lis.sort(reverse=True)
print(lis)
lis2_eror = [42,67,90]
lis2_normal = lis2_eror
lis2_normal.append(101)
print(lis2_eror)
print(lis2_normal)#Виводить [42, 67, 90, 101], тому що lis2_normal і lis2_eror це посилання на один і той же список який є в пам'яті і він діє на них обох однаково.
print("\n")
print(f"Копіювання списку за допомогою методу copy()")
lis3 = [42,67,90]
lis3_ok = lis3.copy()
lis3_new = lis3.copy()
lis3_new.append(101)
print(f"lis3: {lis3}")#оргнінальний список
>>>>>>> b13a8fbef3ff269eace11adb4b8db262612244a7
print(f"lis3_ok: {lis3_new}")#Виводить окремо для цього списку 101 