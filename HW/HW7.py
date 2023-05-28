Ain=str( input() )
Bin=str( input() )

listA=list(Ain)
listB=list(Bin)

listC=listA+listB
print(listC)

a1=str( input() )
a2=str( input() )

listA.remove(a1)
listA.append(a2)

b1=str( input() )
print(listB.count(b1))

b2=str( input() )
listB.remove(b2)

print(listA)
print(listB)