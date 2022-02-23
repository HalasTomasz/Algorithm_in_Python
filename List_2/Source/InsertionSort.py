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