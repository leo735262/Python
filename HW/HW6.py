n=str( input() )
a1=int( input() )
a2=int( input() )
b1=int( input() )
b2=int( input() )
c=", "
a=n[a1:a2]
b=n[b1:b2]
print("a="+str(a)+c+"b="+str(b))
print(int(a)>int(b))
print(int(a)<=int(b))
print(int(a)!=int(b))
