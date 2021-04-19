def mergeSort(array):
    
    comparing=0
    changes=0
    
    if len(array)>1:
        
        mid=len(array)//2
        left = array[:mid]
        right = array[mid:]
        
        arr1 = mergeSort(left)
        comparing += arr1[0]
        changes += arr1[1]
            
        arr2 = mergeSort(right)
        comparing += arr2[0]
        changes += arr2[1]
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            comparing+=1
            if left[i] < right[j]:
              changes+=1
              array[k] = left[i]
              i += 1
            else:
                changes+=1
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            changes+=1
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            changes+=1
            array[k]=right[j]
            j += 1
            k += 1
            
    return comparing,changes