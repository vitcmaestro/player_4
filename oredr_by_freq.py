import collections
import operator
n = int(input(""))
a = list(map(int,input().split()))
freq = collections.Counter(a)
sortfreq = sorted(freq.items(),key= lambda x: (x[1],x[0]),reverse = True)
for i in range(len(sortfreq)-1):
    print(sortfreq[i][0],end = " ")
print(sortfreq[-1][0],end ="")
