import math
import sys
def least():
    num1, num2 = map(int,sys.stdin.readline().split())
    i = 2
    least = 1
    while True:
        if num1 < i or num2 < i:
            least = least * num1 * num2
            break
        elif num1 % i == 0 and num2 % i == 0:
            num1 = num1 / i
            num2 = num2 / i
            least *= i
        else:
            i = i + 1
            continue        
    print(math.floor(least))    

cnt = int(input())
for i in range(cnt):    
    least()