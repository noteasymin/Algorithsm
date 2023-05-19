import sys
input = sys.stdin.readline

t = int(input())
s = input().rstrip()
answer = 0


for i in range(len(s)):
    answer += (ord(s[i])-96) * (31**i)

print(answer % 1234567891)