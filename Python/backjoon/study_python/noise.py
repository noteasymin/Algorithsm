def calc():
    num1 = int(input())
    op = input()
    num2 = int(input())
    
    if op == '+':
        sum = num1 + num2
    elif op == '*':
        sum = num1 * num2
    print(sum)

calc()