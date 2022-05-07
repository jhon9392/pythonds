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

def bubbleSort1(alist):
    exchanges = True
    l = len(alist)-1
    while l > 0 and exchanges:
        exchanges = False
        for i in range(l):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        l = l -1
    print(alist)
    return alist
bubbleSort([10,9,8,7,6,5,4,3,2,1])
        
