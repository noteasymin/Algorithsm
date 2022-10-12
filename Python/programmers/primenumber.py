from itertools import permutations
import math

def check(n):


def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join,permutations(list(numbers))))