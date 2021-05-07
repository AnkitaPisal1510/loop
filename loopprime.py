#prime no
# n=int(input("enter:"))
# i=1
# c=1
# while i<n:
#     if n%i==0:
#         c+=1
#     i+=1
# if n==1:
#     print(n,"is integer is not prime")
# elif c==2:
#     print(n,"is prime no")
# else:
#     print(n,"is not prime")




i=1
c=1
while i<=100:
    if i%i==0 :
        c+=1
    i+=1
if c==2:
    print(i,"is prime")
else:
    print(i,"not prime")

