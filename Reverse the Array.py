arr = [1, 2, 3, 4, 5, 6, 7]

def reversearray(arr):

    n = len(arr)
    left = 0
    right = n-1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left = left + 1
        right = right - 1
print(arr)
reversearray(arr)
print(arr)



