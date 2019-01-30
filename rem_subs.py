s1 = input("")
s = input("")
x = s1.find(s)
s2 = ""
for i in range(len(s1)):
    if(i<x or i>(x+len(s))):
        s2 = s2+s1[i]
print(s2.strip())
    
    
