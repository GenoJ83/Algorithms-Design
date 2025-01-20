def mergesort(array):
    if len(array)>1:
        mid = len(array)//2
        left=array[:mid]
        right=array[mid:]
        mergesort(left)
        mergesort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                array[k]=left[i]
                i+=1
                k+=1
            else:
                array[k]=right[j]
                j+=1
                k+=1

        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1
    return array

array= [45,3,5,6,9,8,1]
sorted=mergesort(array)
print(f"Sorted array:{sorted}")
            

    