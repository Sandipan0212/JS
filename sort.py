def merge(a1,a2,a):
    n = len(a1)
    m = len(a2) 

    i = 0
    j = 0
    k = 0

    while i < n and j < m:
        if a1[i] < a2[j]:
            a[k] = a1[i] 
            i = i + 1
            k = k+1
        else:
            a[k] = a2[j] 
            k = k + 1
            j = j+1

    while i < n:
        a[k] = a1[i] 
        i = i + 1
        k = k+1
    while j < m:
        a[k] = a1[j] 
        j = j + 1
        k = k+1 

def marge_sort(a):

    if len(a) == 0 or len(a) == 1:
        return
    
    mid = len(a) // 2
    
    a1 = a[:mid]
    a2 = a[mid:] 
    marge_sort(a1)
    marge_sort(a2)
    merge(a1,a2,a) 


def partition(a,si,ei):

    pivot = a[si] 
    c = 0
    i = si
    j = ei
    while i < j:
        if pivot > a[i+1]:
            c = c+1
        i = i + 1
    a[si+c],a[si] = a[si],a[si+c] 
    index = si + c

    while si < index and index < ei:
        if a[si] < a[index]:
            si = si + 1
        elif a[ei] > a[index]:
            ei = ei - 1
        else: 
            a[si],a[ei] = a[ei],a[si] 
    return index

def quick_sort(a,si,ei):
    if si >= ei:
        return
    index = partition(a,si,ei)
    quick_sort(a,si,index-1) 
    quick_sort(a,index+1,ei)




a = [10,9,8,7,6,5,4,3,2,1]
quick_sort(a,0,len(a)-1) 
print(a)

b = [10,9,8,7,6,5]
marge_sort(b)
print(b)