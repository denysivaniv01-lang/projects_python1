stack = []

def push(stack,add):
    stack.append(add)

push(stack,67)
push(stack,69)
push(stack,1488)
print(f"Додано елементів:{stack}")
stack.pop()
print(f"видалено елементів:{stack}")
def peek(stack,num):
    return stack[num]
print(f"Перший елемнт:{peek(stack,0)}")