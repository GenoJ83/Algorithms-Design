def quicksort(array):
    if len(array)<=1:
        return array
    pivot = array [len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right=[x for x in array if x>pivot]
    return quicksort(left)+middle+quicksort(right)
array= [45,3,5,6,9,8,1]
sorted=quicksort(array)
print(f"Sorted array:{sorted}")
    