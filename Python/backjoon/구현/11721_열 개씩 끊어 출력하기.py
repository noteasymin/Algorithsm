s = input()
n = len(s)//10 + 1

for i in range(0,n):
    print(s[i*10:(i+1)*10])
