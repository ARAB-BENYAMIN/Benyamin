#prime_numbers in range
def aval_morabea(num):
    flag= True
    for i in range(2,num):
        if num%i==0:
            flag= False
    else:
        return flag


for i in range (100,1000):
    test=aval_morabea(i)
    if test==True:
        print(i)
