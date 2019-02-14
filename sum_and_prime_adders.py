import math
def isprime(x):
    if(x == 2):
        return True
    elif(x%2 == 0):
        return False
    else:
        for m in range(3,int(math.sqrt(x)+1)):
            if(x%m == 0):
                return False
        else:
            return True
n = int(input())
mid = (n//2)+1
for i in range(2,mid):
    j = n-i
    if(isprime(i) and isprime(j)):
        print(i,j)
        break
