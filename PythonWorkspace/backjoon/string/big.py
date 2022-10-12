def compare():
    while True:
        num1, num2 = map(int,input().split(" "))

        if num1 > num2:
            print("Yes")
        elif num1 == 0 and num2 == 0:
            break
        else:
            print("No")
        
compare()