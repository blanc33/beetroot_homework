def bubbleSort_UpDown(alist):
    up=True
    d=0
    f=len(alist)-1
    while d<f :
        if up==True :
            for i in range(d,f,1):
                if alist[i]>alist[i+1]:
                    alist[i+1],alist[i]=alist[i],alist[i+1]
            f-=1
            up=False
        else:
            for i in range(f,d,-1):

                if alist[i]<alist[i-1]:
                    alist[i-1],alist[i]=alist[i],alist[i-1]
            d+=1
            up=True
    return L

L=[10,9,8,7,6,5,4,3,2,1,0]

print("UnSorted list:", L)
sorted=bubbleSort_UpDown(L)
print("Sorted list:", sorted)
