import csv

f=open("data.csv","r")
rd=csv.reader(f,delimiter=",")
head=next(rd)
data=[]
for row in rd:
    data.append(row)
n=len(data)
m=len(data[0])
for i in range(len(data)):
    for j in range(len(data[i])):
    	data[i][j]='%.3f'%float(data[i][j])

for i in range(len(data)):
    for j in range(len(data[i])):
        if j==len(data[i])-1:
            print(data[i][j])
        else:
            print(data[i][j],end=' ')
k=10911107%m
max=data[0][k]
for i in range(len(data)):
	if max<data[i][k]:
		max=data[i][k]
print(max)