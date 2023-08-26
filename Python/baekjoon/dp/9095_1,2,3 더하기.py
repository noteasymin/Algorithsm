def solution():
    arr = [1, 2, 4, 7]
    cal = [1, 2, 3]
    for i in range(4, 10):
        arr.append(sum(cal[-3:]) + arr[-1])
        cal.append(arr[-1] - arr[-2])

    t = int(input())

    for _ in range(t):
        num = int(input())
        print(arr[num - 1])


solution()
