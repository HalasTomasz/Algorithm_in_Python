
def BSearch(arr,valuve,comp):
    comparing = comp
    
    if arr is None or len(arr) == 0:
        return 0,comparing
    comparing +=1
    if(arr[len(arr)//2]  == valuve):
        return 1,comparing
    if len(arr) == 1 :
        return 0,comparing
    
    comparing +=1
    if (arr[len(arr)//2] < valuve):
        return BSearch(arr[len(arr)//2 :len(arr)], valuve,comparing)
    else:
        return BSearch(arr[0:len(arr)//2], valuve,comparing)
  
   

