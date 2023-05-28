#實作函式
def extract_even(L):
    c=[]
    for i in range(len(L)) :
        for j in range(len(L[i])) :
             if (L[i][j]%2)==0 &(L[i][j]/2!=0) :
                 c.append(L[i][j])
    return c

#以下是題目
A=[]
nRow=eval(input())

for i in range(nRow):
  line=input()
  A.append([int(v) for v in line.split(sep=',')])

A_even=extract_even(A)
print("output:", A_even)