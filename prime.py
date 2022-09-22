def prime (n):
    f=0
    for i in range (2,n):
        if(n%i==0):
            f=1 
        return f
n=int(input("enter no"))
m=prime(n)
if m==0:
    print("prime no")
else:
    print("not prime")