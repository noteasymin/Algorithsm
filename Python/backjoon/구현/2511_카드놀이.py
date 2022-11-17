lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
answer = [0, 0]
who = []
for i in range(10):
    if lst1[i] > lst2[i]:
        answer[0] += 3
        who.append('A')
    elif lst2[i] > lst1[i]:
        answer[1] += 3
        who.append('B')
    else:
        answer[0] += 1
        answer[1] += 1
        who.append('D')

print(answer[0],answer[1])

if answer[0] == 10 and answer[1] == 10:
    print('D')
elif answer[0] > answer[1]:
    print('A')
elif answer[0] < answer[1]:
    print('B')
elif answer[0] == answer[1]:
    for i in reversed(who):
        if i == 'A':
            print('A')
            break
        elif i == 'B':
            print('B')
            break
        else:
            continue