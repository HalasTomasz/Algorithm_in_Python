def quickSort(array, leftIdx, rightIdx):
    comparing = 0
    changes = 0
    if(rightIdx > leftIdx):
        i = leftIdx - 1
        j = rightIdx + 1
        
        pivot = array[ (leftIdx + rightIdx) // 2 ]
        while (True):
            i+=1
            comparing += 1
            while(pivot > array[i]):
                i += 1
                comparing += 1
            j -= 1
            comparing += 1
            while(pivot < array[j]):
                j -= 1
                comparing += 1
            if (i <= j):
                changes += 2
                array[i], array[j] = array[j], array[i]    
            else:
                break

        if (j > leftIdx): 
            array1 = quickSort(array, leftIdx, j)
            comparing += array1[0]
            changes += array1[1]
        if (i < rightIdx): 
            array2 = quickSort(array, i, rightIdx)  
            comparing += array2[0]
            changes += array2[1]       
    return comparing, changes