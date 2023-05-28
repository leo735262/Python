def filter(data,threshold=60):
    #newgrade=[x for x in grades if x>= threshold]
    #return newgrade
    newdata=[]
    for i in range(len(data)):
        if data[i]>=threshold :
            newdata.append(data[i])
    return newdata

def genData(seed,N): 
    import random
    random.seed(seed)
    L=[ random.randint(0,100) for _ in range(N) ]
    return L