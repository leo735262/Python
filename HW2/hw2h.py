import csv
with open('data.csv','r')as csvfile:
    rows=csv.reader(csvfile,delimiter=',')
    head=next(rows)
    max=float('-inf')
    for row in rows:
        k=10911107%len(row)
        for i in range(len(row)):
            row[i]='%.3f'%float(row[i])  
            if max<float(row[k]):
                max=float(row[k])
        print((((str(row).replace(","," ")).replace("'","")).replace("[","")).replace("]",""))
    print('%.3f'%float(max))