arr = [5, 10, 15, 20, 25, 30, 35]

def binary_search_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1


print(binary_search_iterative(arr, 25))
print(binary_search_iterative(arr, 40))

arr = [10, 25, 30, 45, 50]  
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1
print(linear_search(arr, 30))
print(linear_search(arr, 99))