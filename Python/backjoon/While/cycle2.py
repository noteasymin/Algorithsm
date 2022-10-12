import sys

originalNumber = int(sys.stdin.readline())
N1 = str(originalNumber)
N2 = 0
N3 = 0
sum = 0
cnt = 0

if(originalNumber < 10):
    N2 = "0"
    N3 = N1
    cnt += 1
else:
    N2 = N1[0:1]
    N3 = N1[1:2]
    cnt += 1

sum = int(N2) + int(N3)
sumstr = str(sum)
print(sumstr)
