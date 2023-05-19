def plus(num):
    if(int(num) > 9):
        num = str(num)
        num1 = int(num[0])
        num2 = int(num[1])
        num3 = num1+num2
    else:
        num = str(num)
        num3 = num + num
        return int(num3)
    
    if(num3 > 9):
        num3 = str(num3)
        num3 = num3[1]
        num3 = str(num3)
    else:
        num3 = str(num3)

    num2 = str(num2)
    num = int(num2+num3)
    
    return num

original_num = input()
result = plus(original_num)
cnt = 1
while True:
    if int(original_num) == result:
        print(cnt)
        exit()
    else:
        result = plus(result)
        cnt += 1


