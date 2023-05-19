def check():
    while True:
        num1, num2 = map(int, input().split(" "))
        if num2 > num1:
            if num2 % num1 == 0:
                print("factor")
            else:
                print("neither")
        elif num1 > num2:
            if num1 % num2 == 0:
                print("multiple")
            else:
                print("neither")
        elif num1 == 0 and num2 == 0:
            break

        
check()

