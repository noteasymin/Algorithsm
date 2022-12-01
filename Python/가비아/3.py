import bisect
def solution(p):
    dp = [p[0]]

    for i in range(len(p)):
        if p[i] > dp[-1]:
            dp.append(p[i])
        else:
            idx = bisect.bisect_left(dp,p[i])
            dp[idx] = p[i]
    print(len(dp))
solution([3,2,1,4,5])