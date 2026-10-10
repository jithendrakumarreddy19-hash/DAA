
# Selection Sort on Different Arrays

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


random_arr = [40, 10, 30, 20, 50]
reverse_arr = [50, 40, 30, 20, 10]
sorted_arr = [10, 20, 30, 40, 50]

print("Random Array:", selection_sort(random_arr))
print("Reverse Array:", selection_sort(reverse_arr))
print("Sorted Array:", selection_sort(sorted_arr))
