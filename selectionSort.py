def selectionSort(alist):
    
    for i in range(len(alist)-1,0,-1):
        maxposition = 0
        for j in range(1,i+1):
            if alist[j] > alist[maxposition]:
                
                maxposition = j
                
        temp = alist[i]
        alist[i] = alist[maxposition]
        alist[maxposition] = temp
        print(alist)    
        
selectionSort([10,9,8,7,6,5,4,3,2,1])
        
