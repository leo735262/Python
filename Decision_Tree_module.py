import numpy as np
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris_data=load_iris()
x=iris_data.data
y=iris_data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=50)

train_accuracy=[]
test_accuracy=[]
dt=DecisionTreeClassifier(criterion="entropy")
dt.fit(x_train,y_train)
print(f"Accuracy={dt.score(x_test,y_test)}")
tree.plot_tree(dt)
plt.show()