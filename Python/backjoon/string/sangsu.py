import sys

def max_number():
    num = list(sys.stdin.readline().split(" "))

    num[0] = num[0].strip()
    num[1] = num[1].strip()
    num[0] = num[0][::-1]
    num[1] = num[1][::-1]      
    num = list(map(int,num))
    
    print(max(num))
max_number()