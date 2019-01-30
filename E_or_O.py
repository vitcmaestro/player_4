n = int(input(""))
summ = 0
while(n>0):
    r = n%10
    if(r%2!=0):
        summ+=r
    n = n//10
if(summ%2 != 0):
    print("O")
else:
    print("E")
