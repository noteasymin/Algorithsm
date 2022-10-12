def three():
    num = list(map(int,input().split()))
    
    largest = max(num)
    lowest = min(num)

    num.remove(largest)

    if largest in num:
        if num[0] > num[1]:
            print(num[1])
            return 0
        else:
            print(num[0])
            return 0
    
    num.remove(lowest)

    if lowest in num:
        print(lowest)
        return 0
    
    print(num[0])
    
three()