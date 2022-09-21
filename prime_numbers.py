#prime_numbers in range
def hvhuin(num):
    flag= True
    for i in range(2,num):
        if num%i==0:
            flag= False
    else:
        return flag
    
lower = int(input("write your lower number"))
upper = int(input("write your upper number"))

for i in range (lower,upper):
    test=hvhuin(i)
    if test==True:
        print(i)
#it is prime number or not
def check(num):
    flag= True
    for i in range(2,num):
        if num%i==0:
            flag= False
    else:
        return flag
x= int(input("\t -->"))
test=check(x)
if test==True:
    print("{} is aval".format(x))
elif x<=1:
    print("{} is not aval".format(x))
else:
    print("{} is not aval".format(x))
