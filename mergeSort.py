def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        l = alist[:mid]
        r = alist[mid:]
        mergeSort(l)
        mergeSort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                alist[k] = l[i]
                i += 1
            else:
                alist[k] = r[j]
                j += 1
            k += 1
        while i <len(l):
            alist[k] = l[i]
            i += 1
            k += 1
        while j <len(r):
            alist[k] = r[j]
            j += 1
            k += 1
        # print(alist)
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
        
