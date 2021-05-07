#perfect no is a positive intrger  that is equal to the sum of its positive divisors aslo
# excluding the number itself
#  ex.6 has divisior 1,2 and 3 =1+2+3=6 .6 is perfect no

def p(a):
     i=0
    sum=0
    while i<a:
        if a%i==0:
            print(i)
            sum+=i
        i+=1
    if sum==a:
        print("it is perfect number")
    else:
        print("it is not perfect")
p(48)


