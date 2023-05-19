from calendar import c


def black():
    cnt, maxinum = map(int,input().split())
    cnt_nums = []
    i = j = k = maxi = 0
    cnt_nums = list(map(int,input().split()))

    for i in range(cnt):
        for j in range(i+1,cnt):
            for k in range(j+1,cnt):
                temp = cnt_nums[i] + cnt_nums[j] + cnt_nums[k]
                if maxi < temp:
                    if maxinum >= temp:
                        maxi = temp
                    else:
                        pass
    print(maxi)


black()