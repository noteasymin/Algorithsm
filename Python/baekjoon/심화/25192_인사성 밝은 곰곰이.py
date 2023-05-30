import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    result = set()
    cnt = 0

    for i in range(n):
        nickname = input().rstrip()

        if nickname != 'ENTER':
            if nickname not in result:
                cnt += 1
                result.add(nickname)

        elif nickname == 'ENTER':
            result.clear()

    print(cnt)


solution()
