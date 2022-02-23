def DualPivot(array,left,right):
    
    comparing=0
    changes=0
    if right <= left :
        return comparing,changes
    
    comparing +=1
    if array[right] < array[left]:
        p=array[right]
        q=array[left]
    else:
        p=array[left]
        q=array[right]
    i = left +1
    k = right -1
    j = i
    d = 0 
    while j<=k:
        if d>=0:
            comparing +=1
            if array[j] < p:
                changes +=2
                array[j],array[i]=array[i],array[j]
                i +=1
                j +=1
                d +=1
            else:
                comparing +=1
                if array[j] < q:
                    j +=1
                else:
                    changes +=2
                    array[j],array[k] = array[k],array[j]
                    k -= 1
                    d -= 1
        else:
            comparing +=1
            if array[k] > q:
                k -=1
                d -=1
            else:
                comparing +=1
                if array[k] < p:
                    changes +=3
                    
                    array[i],array[k],array[j]  = array[k],array[j],array[i]
                   
                    i +=1
                    d +=1
                else:
                    changes +=2
                    array[k],array[j]=array[j],array[k]
                j=j+1
    
    changes += 2            
    array[left] = array[i-1] 
    array[i-1]=p
    array[right] = array[k+1]
    array[k+1]=q
    
    answer1 = DualPivot(array, left, i-2)
    answer2 = DualPivot(array, i, k)
    answer3 = DualPivot(array, k +2, right)
    changes = changes + answer1[1] + answer2[1] + answer3[1]
    comparing = comparing + answer1[0] + answer2[0] + answer3[0]
    
    return comparing,changes             