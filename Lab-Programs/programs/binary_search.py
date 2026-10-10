# Binary Search

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter element to search: "))

low = 0
high = n - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position:", mid)
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")