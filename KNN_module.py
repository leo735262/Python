import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris_data=load_iris()
x=iris_data.data
y=iris_data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=50)

train_accuracy=[]
test_accuracy=[]
k_range=range(1,11) # 測試k=1到10

for k in k_range:
    knn=KNeighborsClassifier(k)
    knn.fit(x_train,y_train)
    train_accuracy.append(knn.score(x_train,y_train))
    test_accuracy.append(knn.score(x_test,y_test))

plt.plot(k_range,train_accuracy,label="training accuracy")
plt.plot(k_range,test_accuracy,label="testing accuracy")
plt.xlabel("# of neighbors")
plt.ylabel("accuracy(%)")
plt.legend()
plt.show()
# 如果要直接存檔，使用plt.savefig("knn-demo.png")
