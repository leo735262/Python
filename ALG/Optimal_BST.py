import numpy 
def Optimal_BST(p,q,n):
    e=numpy.zeros((n+2,n+1))    #let e[1...n+1,0...n]
    w=numpy.zeros((n+2,n+1))    #let w[1...n+1,0...n]
    root=numpy.zeros((n+1,n+1))   #let root[1...n,1...n]

    #initialization
    for i in range(1,n+2):
        e[i][i-1]=q[i-1]
        w[i][i-1]=q[i-1]

    #recursive formula
    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            e[i][j]=10000000    #infinite
            w[i][j]=round(w[i][j-1]+p[j]+q[j],2)
            #find root[i][j]
            for r in range(i,j+1):
                t=e[i][r-1]+e[r+1][j]+w[i][j]
                if t<e[i][j]:
                    e[i][j]=round(t, 2)
                    root[i][j]=r

    return e,root,w

try:
    p=[0,0.15,0.1,0.05,0.1,0.2]
    q=[0.05,0.1,0.05,0.05,0.05,0.1]
    n=5
    e,root,w=Optimal_BST(p,q,n)

    print('\n')
    print("e table:")
    for i in range(n+2):
        print(e[i])
    print('\n')
    print("w table:")
    for i in range(n+2):
        print(w[i])
    print('\n')
    print("root table:")
    for i in range(1,n+1):
        print(root[i])

except Exception as e:
    print(str(e))