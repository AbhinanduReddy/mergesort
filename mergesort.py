def merge(l,mid,h):
    
    global a
    
    i=l-1
    j=mid
    b=[0]*h
    k=0
    while i<mid and j<h:
        if a[i]>a[j]:
            b[k]=a[j]
            j=j+1
        else:
            b[k]=a[i]
            i=i+1
        k=k+1
    while i<mid:
        b[k]=a[i]
        i=i+1
        k=k+1
    while j<h:
        b[k]=a[j]
        j=j+1
        k=k+1
    return b
    
def mergesort(l,h):
    b=[]
    if(l<h):
        mid=(l+h)//2
        b=mergesort(l,mid)
        b=mergesort(mid+1,h)
        b=merge(l,mid,h)

    return b

if __name__=='__main__':
    a=[1,5,7,0,3,9]
    l=int(1)
    h=int(len(a))
    b=mergesort(l,h)
    print(b)
    








