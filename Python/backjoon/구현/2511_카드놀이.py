lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
answer = [0, 0]
for i in range(10):
    if lst1[i] > lst2[i]:
        answer[0] += 3
    elif lst2[i] > lst1[i]:
        answer[1] += 3
    else:
        answer[0] += 1
        answer[1] += 1

print(answer[0],answer[1])

if answer[0] == 10 and answer[1] == 10:
    print('D')
elif answer[0] > answer[1]:
    print('A')
elif answer[0] < answer[1]:
    print('B')
elif answer[0] == answer[1]:
    if lst1[-1] > lst2[-1]:
        print('A')
    else:
        print('B')