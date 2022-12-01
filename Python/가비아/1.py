from itertools import combinations
def solution(s):
    answer = []
    ans = set()
    result = set()
    for i in range(len(s)):
        for j in range(i,len(s)):
            temp = s[i:j+1]
            ans.add(temp)
    for i in ans:
        if len(i) == len(set(i)):
            result.add(i)
    return len(result)