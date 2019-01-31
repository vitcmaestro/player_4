n = int(input(""))
a = []
for i in range(n):
    s = input("")
    a.append(s)
for i in range(n-1):
    if(a[i] == a[i+1]):
        print("yes")
        break
else:
    print("no")
