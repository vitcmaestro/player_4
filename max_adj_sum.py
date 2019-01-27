n = int(input())
a = list(map(int,input().split()))
a.remove(a[0])
print(sum(a))
