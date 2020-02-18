# TO-DO: complete the helpe function below to merge 2 sorted arrays
# O(n log n)

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = j = k = 0
    while i < len(arrA) and j < len(arrB):
        #Check if index i in arrA is smaller than index j in arrB
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i] #If this is true then add add the value in index i to the merged array 
            i +=1 # Next i 
        else:
            merged_arr[k] = arrB[j] #If this is true then add add the value in index j to the merged array 
            j += 1 #Next j 
        k += 1 #To move k index after comparison
    
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Create a base casae
    if len(arr) <=1:
        return arr
    else:
        half = len(arr)//2 #Cut array in half
        #New Arrays to be sorted
        L = merge_sort(arr[:half])
        R = merge_sort(arr[half:])

        arr = merge(L, R)
    

    return arr

merge_sort([2,6,4,5])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
