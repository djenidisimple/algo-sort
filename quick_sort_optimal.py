import random

def partition(array, start, end):
    pivot = array[random.randint(start, end)]
    j = start
    for i in range(start, end):
        if array[i] <= pivot:
           array[i], array[j] = array[j], array[i]
           j+=1
    array[j], array[end] = array[end], array[j]
    return j

def quick_sort_algo(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quick_sort_algo(array, start, pivot - 1)
        quick_sort_algo(array, pivot + 1, end)
    return array

def quick_sort(array):
    array_sort = quick_sort_algo(array, 0, len(array) - 1)
    return array_sort

print(quick_sort([6, 5, 3, 1, 4, 2, 7]))