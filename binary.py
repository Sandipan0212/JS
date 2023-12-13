def binary_search(a,data):
    si = 0
    ei = len(a)
    while si <= ei:
        mid = (si+ei) // 2
        if a[mid] < data:
            si = mid + 1
        elif a[mid] > data:
            ei = mid - 1
        else:
            return mid 
    return -1 

a = [1,2,3,4,5,6,7,8,9]
b = binary_search(a,1)


def print1ton(n):
    if n == 0 :
        return 
    
    print(n)
    print1ton(n-1)

def linear_search(a,val,i=0):
    
    if i == len(a):
        return -1
    
    elif a[i] == val:
        return i
   
    else:
        return linear_search(a,val,i+1) 
    
        
        
index=linear_search([4,5,6,7,8,9],10)
print(index)




