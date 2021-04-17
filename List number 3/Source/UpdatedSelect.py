import numpy as np
def Select2(A,i,comp,chan):
    global checker
    comparing = comp
    changes = chan
    
    arr_of_x = [A[i:i+checker] for i in range(0,len(A),checker)]
    
    for el in arr_of_x:
        compIns,chanIns = insertionSort(el)
        comparing += compIns
        changes += chanIns
        
    sorted_arr = [x for x in arr_of_x]
    medians_arr = [el[len(el)//2] for el in sorted_arr]
 
    if len(medians_arr) <= checker:
        pivot = sorted(medians_arr)[len(medians_arr) // 2]
    else:
        pivot,compar1,chang1 = Select2(medians_arr,len(medians_arr) // 2,comparing,changes)
        
    p,comp2,chang2 = partition(A, pivot)
    comparing += comp2
    changes += chang2
    
    if i == p:
        return A[i],comparing,changes
    elif i < p:
        return Select2(A[0:p], i,comparing,changes)
    else:
        return Select2(A[p+1:len(A)], i - p - 1,comparing,changes)
    

def partition(arr, pivot):
    comparing=0
    changes=0
    left = 0
    right = len(arr) - 1
    i = 0
        
    while i <= right:
        if arr[i] == pivot:
            comparing +=1
            i += 1

        elif arr[i] < pivot:
            comparing +=2
            changes +=2
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            comparing +=2
            changes +=2
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
            
    return left,comparing,changes

def insertionSort(array):
    comparing=0
    changes=0
    for x in range(1,len(array)):
        key = array[x]
        i=x-1
        comparing +=1
        while i >= 0 and array[i]>=key :
            comparing +=1
            changes +=1
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key
        
    return comparing,changes  


