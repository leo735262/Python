product={"pineapple":10, "apple":10, "orange":10}
Name=str(input())
Doing=str(input())
Num=int(input())
if Name=='pineapple':
    if Doing=='stock':
     product["pineapple"]+=Num
    elif Doing=='sell':
     product["pineapple"]-=Num
print(product["pineapple"])
if Name=='apple':
    if Doing=='stock':
     product["apple"]+=Num
    elif Doing=='sell':
     product["apple"]-=Num
print(product["apple"])
if Name=='orange':
    if Doing=='stock':
     product["orange"]+=Num
    elif Doing=='sell':
     product["orange"]-=Num
print(product["orange"])