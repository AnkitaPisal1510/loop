#factor of no
n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    if n%i==0:
        print(i)
        sum+=1
    i+=1