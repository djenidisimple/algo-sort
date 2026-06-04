def test_sort(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False 
    return True

def bubble_sort(array):
    is_sort = test_sort(array)
    while not is_sort:
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        is_sort = test_sort(array)
    return array

print("Bubble Sort\n")
print("Unsorted array: [5, 2, 9, 1, 5, 6]")
print("Sorted array: ", end="")
print(bubble_sort([5, 2, 9, 1, 5, 6]))