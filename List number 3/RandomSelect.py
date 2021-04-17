import numpy as np

def random_select(A,p,q,i,comp,chan):
    comparing = comp
    changes = chan
    if p == q:
        return A[p],comparing,changes
    
    r,comp2,chan2 = partitionrand(A,p,q)
    comparing += comp2
    changes += chan2
    
    k = r - p +1

    if i == k:
        return A[r],comparing,changes
    elif i < k:
      value,comp1,chan1 = random_select(A,p,r-1,i,0,0)
    else:
      value,comp1,chan1 = random_select(A,r+1,q,i-k,0,0)
    comparing +=comp1
    changes +=comp1
    return value,comparing,changes
    

def partitionrand(arr , start, stop):
    #Seed
    randpivot = np.random.randint(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    
    return partition(arr, start, stop)
 

def partition(arr,start,stop):
    comparing = 0
    changes = 0
    pivot = start 
    i = start + 1
    
    for j in range(start + 1, stop + 1):
        comparing +=1
        if arr[j] <= arr[pivot]:
            changes +=2
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    changes +=2
    changes +=2 #Rand
    pivot = i - 1
    return pivot,comparing,changes
               
      
#%%
A = [*range(100,0,-1)]
print(random_select(A, 0, len(A)-1, 0,0,0))