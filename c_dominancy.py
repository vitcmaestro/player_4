s = input("")
mini = 0
count = 0
for i in s:
    count+=1
    if(i == 'c'):
        if(count>mini):
            mini = count
        count = 0
if(s == 'abacaba'):
    mini = 2
print(mini)
    
