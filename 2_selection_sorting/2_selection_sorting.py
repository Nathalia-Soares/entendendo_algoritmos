def minorSearch(arr):
    minor = arr[0]
    minorIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minorIndex = i
    return minorIndex

def selectionSort(arr):
    newArr = []
    for i in  range(len(arr)):
        minor = minorSearch(arr)
        newArr.append(arr.pop(minor))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))