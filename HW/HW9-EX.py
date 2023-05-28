value=eval(input())

try:
    if value >= 0:
        print(value)
    else:
        raise ValueError("no negative value!")
    
    print('the program te1rminated normally')
except ValueError as err:
    print(err)