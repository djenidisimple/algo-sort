def merge(left=[], right=[]):
    new_array = []
    i = 0 
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_array.append(left[i])
            i+=1
        else:
            new_array.append(right[j])
            j+=1
    return new_array + left[i:] + right[j:]
    
def merge_sort(array):
    if len(array) <= 1:
        return array
    left, right = array[:len(array) // 2], array[len(array) // 2:]
    sort_left = merge_sort(left)
    sort_right = merge_sort(right)
    return merge(sort_left, sort_right)
print(merge_sort([6, 5, 3, 1, 4, 2, 7]))