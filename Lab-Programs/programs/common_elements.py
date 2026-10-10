# Find common elements between two arrays

n = int(input("Enter size of first array: "))
arr1 = []

for i in range(n):
    arr1.append(int(input("Enter element: ")))

m = int(input("Enter size of second array: "))
arr2 = []

for i in range(m):
    arr2.append(int(input("Enter element: ")))

print("Common elements:")

for i in arr1:
    for j in arr2:
        if i == j:
            print(i)
            break