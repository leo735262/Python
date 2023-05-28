def quicksort(A,p,r):
    if p<r :
        q=partition(A,p,r)
        #---------------------------------------------------
        print("partition:"+str(A[q]),end='')
        print("\n=>sort:",end='')
        for i in range(0,int(p/2)):
            print("\t   ",end='')
        for i in range(p,r+1):
            if i<r :
                print(str(A[i])+"->",end='')
            else:
                print(str(A[i]),end='')
        print("\n")
        #---------------------------------------------------
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition(A,p,r):
    print( "(start:"+str(p)+",end:"+str(r)+")" ,end='')
    x=A[r]
    i=p-1

    for j in range(p,r):
        if A[j]<=x :
            i=i+1

            box=A[i]#exchange A[i] with A[j](把小於partition的數往又擺)
            A[i]=A[j]
            A[j]=box
        
    

    box=A[i+1]#exchange A[i+1] with A[r](把partition放在正確的位子)
    A[i+1]=A[r]
    A[r]=box

    return i+1

#主程式

#---------------------------------------------------
n=8
A=[2,8,7,1,3,5,6,4,]
print("原:",end='')
for i in range(0,n):
    if i<n-1:
        print(str(A[i])+'=>',end='')
    else:
        print(str(A[i]),end='')
print("\n")
#---------------------------------------------------

quicksort(A,0,n-1)

for i in range(0,n):
    print(A[i],end='') 
    print(',',end='')