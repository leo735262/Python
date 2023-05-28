import csv
import numpy as np
from math import log
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

try:
    f=open("data.csv","r")
    rd=csv.reader(f,delimiter=",")
    head=next(rd)
    data=[]
    cleared_data=[]
    for row in rd:
        data.append(row)
    #print(data)
    #將數值資料從string轉型成float
    for i in range(len(data)):
        for j in range(len(data[i])-1):
            if data[i][j]!='?':
                data[i][j]=float(data[i][j])

    #  A---描述資料集的欄位數，資料筆數，以及是否有missing data---
    count_t=0   #missing data的格數
    f=0
    count_p=0   #有missing data的資料筆數
    for i in range(len(data)):
        for j in data[i]:
            if j=='?':
                count_t=count_t+1
                f=1
        if f==1:
            count_p=count_p+1
        else:
            #處理missing data by Complete cases analysis
            cleared_data.append(data[i])
        f=0
    print(f"A:\n資料集的欄位數:{len(data[0])}\n"
        +f"資料筆數:{len(data)}\n"
        +f"missing data的格數:{count_t}\n"
        +f"有missing data的資料筆數:{count_p}")
    #--------------------------------------------------------
    #  B--列出不同數值的數量與所佔比例
    class_column=[]
    for i in range(len(data)):
            class_column.append(data[i][len(data[i])-1])
    value, counts = np.unique(class_column, return_counts=True)
    print("B:\nclass欄位中各數值出現次數:", dict(zip(value, counts)))
    print("class欄位中各數值出現比例:", dict(zip(value, counts/len(data))))
    #根據a的分佈計算此欄位的entropy
    probs=counts/len(class_column)  # numpy陣列可以直接除以一個數值
    entropy=sum(-p*log(p,2) if p>0 else 0 for p in probs)
    print(f"class欄位的entropy:{entropy}")
    #--------------------------------------------------------
    #  C--建立Decision Tree模型並回報模型的準確度

#****************將資料切成訓練/測試的地方(以下)****************
    #將data、target分開
    data_information=[]
    data_class=[]
    for i in range(len(cleared_data)):
        data_information.append(cleared_data[i][0:-1])
        data_class.append(cleared_data[i][len(cleared_data[i])-1])
    #切分訓練、測試資料
    x_train,x_test,y_train,y_test=train_test_split(data_information,data_class,test_size=0.2,random_state=50)
#****************將資料切成訓練/測試的地方(以上)****************
#****************產生模型與訓練模型的的地方(以下)****************
    train_accuracy=[]
    test_accuracy=[]
    dt=DecisionTreeClassifier(criterion="entropy")
    dt.fit(x_train,y_train)
    #******計算(呼叫套件提供方法)準確度******
    print(f"C:\nAccuracy={dt.score(x_test,y_test)}")
    
    #畫數
    tree.plot_tree(dt)
    plt.show()
#****************產生模型與訓練模型的的地方(以上)****************
    
#------------KNN模型------------
    # train_accuracy=[]
    # test_accuracy=[]
    # k_range=range(1,11) # 測試k=1到10

    # for k in k_range:
    #     knn=KNeighborsClassifier(k)
    #     knn.fit(x_train,y_train)
    #     train_accuracy.append(knn.score(x_train,y_train))
    #     test_accuracy.append(knn.score(x_test,y_test))

    # plt.plot(k_range,train_accuracy,label="training accuracy")
    # plt.plot(k_range,test_accuracy,label="testing accuracy")
    # plt.xlabel("# of neighbors")
    # plt.ylabel("accuracy(%)")
    # plt.legend()
    # plt.show()
#--------------------------------

except Exception as e:
    print(e)
