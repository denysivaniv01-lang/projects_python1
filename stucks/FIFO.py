from collections import deque

que = deque()

que.append("customer 1")
que.append("customer 2")
que.append("customer 3")
print(f"Додаєм елемент:{que}\n")
first = deque.popleft(que)
print(f"перший елмент(оброблений) {first}\n")
print(f"Після оброблення залишилось: {que}\n")
if que:
    print(f"Список не пустий:)\n {que}")
else:
    print(f"Список пустий:(\n {que}")