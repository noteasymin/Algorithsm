import sys
def coordinate():
    n = int(sys.stdin.readline())
    coor_list = []
    for i in range(n):
        coor_list.append(list(map(int,sys.stdin.readline().split())))
    coor_list = sorted(coor_list)
    for i in range(n):
        for j in range(2):
            print(coor_list[i][j],end=" ")
        print()

coordinate()
