def insertion_sort(array):
    for i in range(len(array) - 1):
        j = i + 1
        while j > 0:
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array
print("Insertion Sort")
print("Unsorted array: [5, 6, 3, 1, 8, 7, 2, 4]")
print("Sorted array: ", end="")
print(insertion_sort([5, 6, 3, 1, 8, 7, 2, 4]))