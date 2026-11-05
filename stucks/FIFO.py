from collections import deque

que = deque()

def enqueue(add):
    que.append(add)

enqueue("customer 1")
enqueue("customer 2")
enqueue("customer 3")
print(f"Додаєм елемент:{que}\n")

first = deque.popleft(que)
print(f"перший елмент(оброблений) {first}\n")
print(f"Після оброблення залишилось: {que}\n")

def isempty():
    if que:
        print(f"Список не пустий:)\n {que}")
    else:
        print(f"Список пустий:(\n {que}")

isempty()
