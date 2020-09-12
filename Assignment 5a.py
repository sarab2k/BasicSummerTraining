largest= 0
smallest = None
while  True:
    num=input('Enter the number')
    if num == 'done':
        break
    try:
        n=int(num)
    except:
        print("Invalid input")

    if largest<n:
         largest=n
    if smallest == None :
         smallest=n
    elif smallest>n:
         smallest=n
print('maximum is',largest)
print('minimum is', smallest)
