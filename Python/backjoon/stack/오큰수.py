import sys
def big_o():
    cnt = int(sys.stdin.readline())
    num = list(map(int,sys.stdin.readline().split()))
    bigger_lst = []
    for i in range(0,cnt-1):
        for j in range(i,cnt-1):
            if num[j] < num[j+1]:
                if j == cnt-1 and num[j] >= num[j+1]:
                    bigger_lst.append(-1)
                    break
                else:
                    bigger_lst.append(num[j+1])
                    break
        
                
    bigger_lst.append(-1)
    print(bigger_lst)


big_o()
