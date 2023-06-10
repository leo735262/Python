import csv
import math
import statistics
import numpy as np
import seaborn as sns
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

def print_cloumn_stv(cloumn_name,cloumn_data):
    print(f"\n{cloumn_name}欄位中最大值:{max(cloumn_data)}"
          +f"\n{cloumn_name}欄位中最小值:{min(cloumn_data)}"
          +f"\n{cloumn_name}e欄位平均值:{statistics.mean(cloumn_data)}"
          +f"\n{cloumn_name}欄位中位數:{statistics.median(cloumn_data)}"
          +f"\n{cloumn_name}欄位變異數:{statistics.variance(cloumn_data)}"
          +f"\n{cloumn_name}欄位標準差:{statistics.stdev(cloumn_data)}")
    
def convalue_plt_scatter(cloumn_no,cloumn_data):
    plt.figure(figsize=(19,10))
    plt.scatter([j for j in range(len(cloumn_data))],cloumn_data,s=5)
    plt.title(head[cloumn_no], {"fontsize" : 18})  # 設定標題及其文字大小
    plt.savefig(f"scatter chart cloumn {cloumn_no}_{head[cloumn_no]}.jpg",pad_inches=0.0)  
    plt.close()  

try:
    #開檔
    f=open("healthcare-dataset-stroke-data.csv","r")
    rd=csv.reader(f,delimiter=",")
    #不取欄位名稱
    head=next(rd)
    data=[]
    for row in rd:
        data.append(row)

    #去除不可用資料(id欄位、smoking_status:Unknown)
    cleared_data=[]
    for i in range(len(data)):
        if data[i][10]!="Unknown":
            cleared_data.append(data[i][1:len(data[0])])

    
    #取得bmi data的中位數、非數值欄位分布狀況
    D=[ [] for i in range(len(cleared_data[0]))]
    bmi_data=[]
    for i in range(len(cleared_data)):
        if cleared_data[i][8]!="N/A":
            bmi_data.append(float(cleared_data[i][8]))
        for j in range(len(cleared_data[0])):
            D[j].append(cleared_data[i][j])
            
    bmi_mean=float(statistics.median(bmi_data))

    
    for i in [0,2,3,4,5,6,9,10]:
        value, counts = np.unique(D[i], return_counts=True)
        print(f"{head[i+1]}欄位中各值出現次數:", dict(zip(value, counts)))
        print(f"{head[i+1]}欄位中各值出現比例:", dict(zip(value, counts/len(D[i]))))
        #根據分佈計算此欄位的entropy
        probs=counts/len(D[i])  # numpy陣列可以直接除以一個數值
        entropy=sum(-p*math.log(p,2) if p>0 else 0 for p in probs)
        print(f"{head[i+1]}欄位的entropy:{entropy}\n")

        plt.figure(figsize=(6,9))               # 顯示圖框架大小
        plt.pie(counts,                         # 數值
                labels = value,                 # 標籤
                autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位 
                pctdistance = 0.6,              # 數字距圓心的距離
                textprops = {"fontsize" : 12})  # 文字大小

        plt.axis('equal')                        # 使圓餅圖比例相等
        plt.title(head[i+1], {"fontsize" : 18})  # 設定標題及其文字大小
        plt.legend(loc = "best")                 # 設定圖例及其位置為最佳

        #plt.show()
        plt.savefig(f"Pie chart cloumn {i+1}_{head[i+1]}.jpg",     # 儲存圖檔
                    bbox_inches='tight',               # 去除座標軸占用的空間
                    pad_inches=0.0)                    # 去除所有白邊
        plt.close()  


    bmi_count=0   #bmi missing data的格數
    #將數值資料從string轉型成float or int、編碼
    age_cloumn=[]
    avg_glucose_level=[]
    encoding=[{"Female":0,"Male":1,"Other":3},{},{},{}
              ,{"No":0,"Yes":1},{"Never_worked":0,"children":1,"Private":2,"Self-employed":3,"Govt_job":4}
              ,{"Rural":0,"Urban":1},{},{},{"never smoked":0,"formerly smoked":1,"smokes":2},{}]
    for i in range(len(cleared_data)):
        for j in [0,4,5,6,9]:
            cleared_data[i][j]=encoding[j][cleared_data[i][j]]
        for j in [2,3,10]:
            cleared_data[i][j]=int(cleared_data[i][j])
        for j in [1,7]:
            cleared_data[i][j]=float(cleared_data[i][j])
            if j==1:
                age_cloumn.append(cleared_data[i][j])
            if j==7:
                avg_glucose_level.append(cleared_data[i][j])


        if cleared_data[i][8]!="N/A":
            cleared_data[i][8]=float(cleared_data[i][8])
            bmi_count=bmi_count+1
        else:
            #將bmi missing data 填入bmi data的中位數
            cleared_data[i][8]=bmi_mean

    age_cloumn.sort()
    avg_glucose_level.sort()
    bmi_data.sort()

    print_cloumn_stv("age",age_cloumn)
    print_cloumn_stv("avg_glucose_level",avg_glucose_level)
    print_cloumn_stv("bmi",bmi_data)

    convalue_plt_scatter(2,age_cloumn)
    convalue_plt_scatter(8,avg_glucose_level)
    convalue_plt_scatter(9,bmi_data)

    print(f"\n資料集總欄位數:{len(head)}\n"
        +f"資料集取用欄位數:{len(cleared_data[0])}\n"
        +f"原始資料筆數:{len(data)}\n"
        +f"可用資料筆數:{len(cleared_data)}\n"
        +f"不可用資料筆數(smoking_status:Unknown):{len(data)-len(cleared_data)}\n"
        +f"bmi值無遺失的資料筆數:{bmi_count}")

    #建立Decision Tree模型並回報模型的準確度
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
    accuracy_plt=[]
    for i in range(1001):
        dt=DecisionTreeClassifier(criterion="entropy")

        dt.fit(x_train,y_train)
        #******計算(呼叫套件提供方法)準確度******
        #print(f"{i}. Accuracy={dt.score(x_test,y_test)}")
        accuracy_plt.append(dt.score(x_test,y_test))
        if dt.score(x_test,y_test)>0.9:
            #畫數
            plt.figure(figsize=(19,10))
            tree.plot_tree(dt,fontsize=6)
            plt.savefig(f'tree_high_dpi{math.ceil(dt.score(x_test,y_test)*1000000)}', dpi=100)
            plt.close()  

    accuracy_plt.sort()
    print("最高準確度:"+str(max(accuracy_plt)))
    print("最低準確度:"+str(min(accuracy_plt)))
    plt.figure(figsize=(19,10))
    plt.scatter([j for j in range(len(accuracy_plt))],accuracy_plt,s=5)
    plt.title("Decision Tree accuracy test 1000 times", {"fontsize" : 18})  # 設定標題及其文字大小
    plt.savefig(f"Decision Tree accuracy test 1000 times(scatter).jpg",pad_inches=0.0)  
    plt.close()  

#****************產生模型與訓練模型的的地方(以上)****************
    
    #------------KNN模型------------
    k_range=range(1,16) # 測試k=1到10
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
    plt.savefig("KNN.jpg") 
    #plt.show()
    plt.close()  

    #--------------------------------
except Exception as e:
    print(e)
