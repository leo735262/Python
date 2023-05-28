import numpy as np
from math import log
from sklearn.datasets import load_iris

# 傳入各種事件出現次數, 須加入檢查0機率(出現0次)的機制
def entropy(count):
    s=sum(count)
    if s==0:
        return 0    # count都是0
    
    # 計算各數值出現機率
    probs=np.array(count)/s # 如此保證分母s不等於0
    return sum(-p*log(p,2) if p>0 else 0 for p in probs)

iris_data=load_iris()
x=iris_data.data
y=iris_data.target
f=[[f[i] for f in x] for i in range(0,4)]
for i in range(0,4):
    value,count=np.unique(f[i],return_counts=True)
    print(f"entropy of the {i}-th feature is {entropy(count)}")