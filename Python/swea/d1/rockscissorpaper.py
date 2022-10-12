A, B = map(int,input().split())

if A == 1: # rock
    if B == 3: # scissor
        print('A')
    if B == 2: # paper
        print('B')
elif A == 2: # scissor
    if B == 3: # rock
        print('B')
    if B == 1: # paper
        print('A')
else: # paper
    if B == 2: # rock
        print('A')
    if B == 1: # scissor
        print('B')