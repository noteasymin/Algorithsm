import sys
def alphabet():
    S = sys.stdin.readline().strip()
    ascii = []

    for i in range(97,123):
        ascii.append(chr(i))

    for i in ascii:
        if i in S:
            print(S.index(i),end=" ")
        else:
            print(-1,end=" ")
        

alphabet()