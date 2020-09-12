hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
if h <= 40:
    pay= h*r
    print(pay)
else :
    a=(h-40)
    pay=r*40
    pay=pay+a*1.5*r
    print(pay) 
