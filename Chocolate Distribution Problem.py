arr = [3, 4, 1, 9, 56, 7, 9, 12]
n = len(arr)
m = 5

def findMinDiff(arr,n,m):

    arr.sort()
    min_diff = arr[-1] - arr[0]

    for i in range(0,n-m+1):
        diff = arr[i+m-1]  - arr[i]

        if diff < min_diff:
            min_diff = diff
    return min_diff

print(findMinDiff(arr,n,m))