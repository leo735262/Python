#實作函式
def filter(data,threshold=60):
    #newgrade=[x for x in grades if x>= threshold]
    #return newgrade
    newdata=[]
    for i in range(len(data)):
        if data[i]>=threshold :
            newdata.append(data[i])
    return newdata 


#以下是題目

grades=[]

N=int(input())

for i in range(N):
  grades.append(float(input()))

passed=filter(data=grades)

for v in passed:
  print(v)

passed_grade=float(input())
passed=filter(grades,threshold=passed_grade)
for v in passed:
  print(v)