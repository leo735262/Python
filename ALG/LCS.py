import numpy
def print_LCS(b,X,i,j,LCS):
    if i==0 or j==0:
        return
    
    if b[i][j]==24:
        print_LCS(b,X,i-1,j-1,LCS)  #reverse order
        LCS.append(X[i-1])  #print(X[i-1])
    elif b[i][j]==25:
        print_LCS(b,X,i-1,j,LCS)
    else :
        print_LCS(b,X,i,j-1,LCS)

    return LCS

def LCS_length(X,Y):
    m=len(X)
    n=len(Y)

    b=numpy.zeros((m+1,n+1))    #let b[1...m,1...n]
    c=numpy.zeros((m+1,n+1))    #let c[0...m,0...n]

    #initialization
    for i in range(1,m+1):
        c[i][0]=0
    for j in range(0,n+1):
        c[0][j]=0

    #recursive formula
    for i in range(1,m+1):  #for i=1 to m
        for j in range(1,n+1):  #for j=1 to n
            if X[i-1]==Y[j-1]:  
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=24  #\
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]=25  #|
            else:
                c[i][j]=c[i][j-1]
                b[i][j]=21  #<-

    return c,b

X=['A','B','C','B','D','A','B']
Y=['B','D','C','A','B','A']
LCS=[]
m=len(X)
n=len(Y)

c,b=LCS_length(X,Y)

#print b table
print('\n')
print("b table:")
for i in range(m+1):
    print(b[i])
print('\n')

#print c table
print("c table:")
for i in range(m+1):
    print(c[i])
print('\n')

#print LCS of X and Y
print("LCS of X and Y is:",end='')
LCS=print_LCS(b,X,7,6,LCS)
print(LCS)



