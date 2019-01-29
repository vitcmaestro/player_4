import collections
import operator
n = int(input(""))
a = list(map(int,input().split()))
freq = collections.Counter(a)
sortfreq = sorted(freq.items(),key= operator.itemgetter(1),reverse = True)
print(sortfreq)
for i in range(len(sortfreq)-1):
    if(sortfreq[i][1] == sortfreq[i+1][1] and sortfreq[i][0] <sortfreq[i+1][0]):
        sortfreq[i],sortfreq[i+1] = sortfreq[i+1],sortfreq[i]
    print(sortfreq[i][0],end = " ")
print(sortfreq[-1][0],end ="")
        
