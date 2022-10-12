import sys
input = sys.stdin.readline

def merge_sort(L):
    if len(L) == 1:
        return L

    mid = (len(L) + 1) // 2

    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    i, j = 0, 0
    L2 = []

    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            L2.append(left[i])