s1 = input()
s1 = s1[::-1]
print('-'.join([s1[i:i+1] for i in range(0, len(s1), 1)]))
