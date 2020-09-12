def computepay(h,r):
    if h <= 40:
         pay= h*r
    else :
        a=(h-40)
        pay=r*40
        pay=pay+a*1.5*r
    return pay

hrs = input("Enter Hours:")
h= float(hrs)
rate = input('Enter the rate')
r= float(rate)
p = computepay(h,r)
print("Pay",p)
