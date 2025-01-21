def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example Usage
A = [64, 25, 12, 22, 11]
print("Original Array:", A)
selection_sort(A)
print("Sorted Array:", A)
