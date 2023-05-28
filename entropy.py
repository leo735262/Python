import numpy as np
from math import log
from sklearn.datasets import load_iris

def entropy(x):
    length=len(x)
    # 計算有哪些數值，各出現多少次
    value,count=np.unique(x,return_counts=True)
    probs=count/length  # numpy陣列可以直接除以一個數值
    return sum(-p*log(p,2) if p>0 else 0 for p in probs)

iris_data=load_iris()
x=iris_data.data
y=iris_data.target
f=[[f[i] for f in x] for i in range(0,4)]
for i in range(len(f)):
    print(f"entropy of the {i}-th feature is {entropy(f[i])}")