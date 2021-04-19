import numpy as np 
import time
import json
import InsertionSort as IS
import MergeSort as MS
import Hibrid10 as H
import QuickSort as QS
import DualPivot as DP
def test(name,number):
    A =[]
    for n in range(100,10100,100):
        for k in range(0,number):
            array = np.random.randint(0, 1000, n)
            array1=array.copy()
            array2=array.copy()
            array3=array.copy()
            array4=array.copy()
            array5=array.copy()
            array6=array.copy()
            
            start = time.time()
            comparing,changes=IS.insertionSort(array1)
            end = time.time()
            timer = end - start
            
            data={
                "Tablica":n,
                "Czas":timer,
                "Zmiany":changes,
                "Porownania":comparing,
                "Nazwa":"Insert"
                }
            A.append(data)
            
            start = time.time()
            comparing,changes=MS.mergeSort(array2)
            end = time.time()
            timer = end - start
            
            data={
                "Tablica":n,
                "Czas":timer,
                "Zmiany":changes,
                "Porownania":comparing,
                "Nazwa":"Merge"
            }
            A.append(data)
            
            start = time.time()
            comparing,changes=QS.quickSort(array3, 0, len(array3) -1)
            end = time.time()
            timer = end - start
            
            data={
                "Tablica":n,
                "Czas":timer,
                "Zmiany":changes,
                "Porownania":comparing,
                "Nazwa":"Quick"
            }
            A.append(data)
            
            start = time.time()
            comparing,changes=H.megreInsertSort(array4)
            end = time.time()
            timer = end - start
            
            data={
                "Tablica":n,
                "Czas":timer,
                "Zmiany":changes,
                "Porownania":comparing,
                "Nazwa":"Hibrid10"
            }
            A.append(data)
            
            
            start = time.time()
            comparing,changes=DP.DualPivot(array,0, len(array5) -1)
            end = time.time()
            timer = end - start
           
            data={
                "Tablica":n,
                "Czas":timer,
               "Zmiany":changes,
               "Porownania":comparing,
                "Nazwa":"Dual"
            }
            A.append(data)
    
    try:
        file = open(name, "w")
        json.dump(A,file, indent=3)
    except IOError:
        pass
    finally:
        file.close()   



