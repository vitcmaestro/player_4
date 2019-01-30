import math
def isprime(x):
    if(x == 2):
        return True
    elif(x%2 == 0):
        return False
    else:
        for j in range(3,int(math.sqrt(x)+1)):
            if(x%j == 0):
                return False
        else:
            return True
n = int(input(""))
c = 0
for i in range(2,n+1):
    if(n%i == 0 and isprime(i)):
        if(c == 0):
            print(i,end= "")
            c+=1
        else:
            print("",i,end = "")
    
