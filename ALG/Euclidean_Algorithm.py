def Euclidean_Algorithm(a,b):
    if a>b:
        n=a
        m=b
    else:
        n=b
        m=a

    # if m==0:
    #     return n
    # else:
    #     r=n%m
    #     gcd=Euclidean_Algorithm(m,r)
    #     print("gcd("+str(m)+","+str(n)+")="+str(gcd))
    #     return gcd

    if m!=0:
        r=n%m
        gcd=Euclidean_Algorithm(m,r)
        print("gcd("+str(m)+","+str(n)+")="+str(gcd))
        return gcd
    else:
        return n
    
          
a=int(input())
b=int(input())
r=Euclidean_Algorithm(a,b)
print(r)