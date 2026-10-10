
# Insertion Sort with Duplicate Elements

arr = [5, 2, 4, 2, 3, 5, 1]

n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Sorted Array:", arr)
