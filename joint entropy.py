import numpy as np
from math import log
from sklearn.datasets import load_iris
def joint_entropy(x,y):
    # 計算有哪些數值
    value_x=np.unique(x)
    value_y=np.unique(y)
    probs=[]
    for i in value_x:
        for j in value_y:
            probs.append(np.mean(np.logical_and(x==i,y==j)))
    return sum(-p*log(p,2) for p in probs if p!=0)

iris_data=load_iris()
x=iris_data.data
y=iris_data.target
f=[[f[i] for f in x] for i in range(0,4)]
for i in range(len(f)):
    for j in range(i):
        print(f"H(f[{i}],f[{j}])=-{joint_entropy(f[i],f[j])}")