name=str( input() )
oi=str( input() )
n=int( input() )

product={"pineapple":10, "apple":10, "orange":10}

if oi=='stock':
  if name=='pineapple':
     product['pineapple']+=n

  elif name=='apple':
     product['apple']+=n

  elif name=='orange':
     product['orange']+=n


if oi=='sell':
  if name=='pineapple':
     product['pineapple']-=n

  elif name=='apple':
     product['apple']-=n

  elif name=='orange':
     product['orange']-=n

print(product['pineapple'])
print(product['apple'])
print(product['orange'])
