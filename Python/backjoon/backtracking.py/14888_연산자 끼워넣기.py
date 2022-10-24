import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))
operator_lst = list(map(int, input().split()))


maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
