def bubbleSort(alist):
    
    l = len(alist)
    for j in range(l-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    print(alist)
    return alist
bubbleSort([10,9,8,7,6,5,4,3,2,1])
