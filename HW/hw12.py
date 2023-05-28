from filter import filter
from filter import genData
N=int(input()) 
seed=int(input())
L=genData(seed,N)
passed=filter(data=L,threshold=60)
for v in passed:
  print(v)