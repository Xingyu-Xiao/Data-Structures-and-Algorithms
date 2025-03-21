import bisect
n = int(input())
s = [int(input()) for _ in range(n)]
temp = [0]*n


def sort_arr(arr, left, mid, right):
    i, j, k = left, mid+1, left
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[j] = arr[j]
        j += 1
        k += 1
    for i in range(left, right+1):
        arr[i] = temp[i]


def count(arr, left, mid, right):
    num = 0
    left_arr = arr[left:mid+1]
    for x in arr[mid+1: right+1]:
        num += bisect.bisect_left(left_arr, x)
    return num


def merge(arr, left, right):
    if left >= right:
        return 0
    num = 0
    mid = (left + right) // 2
    num += merge(arr, left, mid)
    num += merge(arr, mid + 1, right)
    num += count(arr, left, mid, right)
    sort_arr(arr, left, mid, right)
    return num


print(merge(s, 0, n-1))
