k1=int( input() )
l=[]
l.append(k1)
while(k1!=0 ):
    key=int( input() )
    k1=key
    if k1>0 :
        l.append(key)
    try:
        if (k1<0) :
            raise ValueError("input error") 
    except ValueError as err: 
        print(err)


k=int( input() )
for v in l :
    
    if ( (v%k==0) & (v/k>=1) ) :
     break
    else:
        print(v)

