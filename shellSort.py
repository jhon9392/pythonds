def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount>0:
        for i in range(sublistcount):
            gapInsertionSort(alist,i,sublistcount)
        sublistcount = sublistcount//2
def gapInsertionSort(alist, start, gap):
    
    for i in range(start+gap, len(alist), gap):
        
        position = i
        val = alist[i]
        while position >= gap and alist[position-1]>val:
            alist[position] = alist[position-1]
            position = position-1
        alist[position]=val

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
        
