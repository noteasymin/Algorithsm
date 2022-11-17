import math
import sys

def dial():
    word = sys.stdin.readline().strip()
    total = 0
    for i in range(len(word)):
        time = (ord(word[i])-59) / 3

        if time == 8 or time >= 10 or time == 9 or time == 11:
            time = time - 1
        
        time = math.floor(time) + 1     
        total += time
        print(time)
        
dial()