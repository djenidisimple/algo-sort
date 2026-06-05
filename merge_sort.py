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
# print(merge_sort([6, 5, 3, 1, 4, 2, 7]))

def merge_div(left_value, right_value):
    return left_value + right_value if left_value <= right_value else left_value - right_value


def divide(array):
     if len(array) == 0:
        return 0
     if len(array) == 2:
        return array[0] + array[1] if array[0] <= array[1] else array[0] - array[1]
     elif len(array) <= 1:
        return array[0]
     left , right = array[:len(array)//2], array[len(array)//2:]
     left_divide = divide(left)
     right_divide = divide(right)
     return merge_div(left_divide, right_divide)
print(divide([10, 1, 100, 10, 1000, 100, 1000, 1000, 1000]))