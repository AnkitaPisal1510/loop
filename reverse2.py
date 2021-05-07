#if we put 123 it will give output 320

n=int(input("enter the number"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev-rem)

# n=int(input("enter the number"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# print(rev//10*10)

#middle number
# n=int(input("enter the number"))
# rev=0
# while n>0:
#     rev=(n%10)+(n%10)+(n%10)
#     n=n//10
# print(rev)

# n=int(input("enter the number"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# print(rev//10*10)