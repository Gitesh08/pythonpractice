
def search(arr, n, x):
    
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1

arr = [4, 67, 34, 23, 54, 49, 18]
n = len(arr)
x = 34

result = search(arr, n, x)

if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)