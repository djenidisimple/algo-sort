def quick_sort(array):
    '''
    Implémentation de trie rapide
    En utilisant le même principre que le trie fusion
    '''
    left, right = [], []
    if len(array) <= 1:
        return array
    pivot = len(array) - 1
    for i in range(len(array) - 1):
        if array[i] < array[pivot]:
            left.append(array[i])
        else:
            right.append(array[i])
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [array[pivot]] + right

print(quick_sort([6, 5, 3, 1, 4, 2, 7]))