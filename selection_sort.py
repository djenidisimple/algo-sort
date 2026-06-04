def selection_sort(array):
    for i in range(len(array)):
        min_array =  i
        for j in range(min_array + 1, len(array)):
            if array[j] < array[min_array]:
                min_array = j
        if min_array != i:
            array[i], array[min_array] = array[min_array], array[i]
    return array

print(selection_sort([5, 6, 3, 1, 8, 7, 2, 4]))