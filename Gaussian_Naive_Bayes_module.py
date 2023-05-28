import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

def run(random_seed=50,tsize=0.15):
    iris_data=load_iris()
    x=iris_data.data
    y=iris_data.target
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=tsize,random_state=random_seed)

    gnb=GaussianNB().fit(x_train,y_train)
    predict=gnb.predict(x_test)
    predict_prob=gnb.predict_proba(x_test)
    print(f"Accuracy={gnb.score(x_test,y_test)}")
    return predict,predict_prob

pred,prob=run()
print(pred,prob)