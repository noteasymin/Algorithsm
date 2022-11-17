from datetime import datetime
import time

n = int(input())
older = 0
younger = 99999999999999999
answer = ['','']
for i in range(n):
    lst = input().split()
    date = []
    date.append(lst[3])
    date.append(lst[2])
    date.append(lst[1])
    date = '-'.join(date)
    tstmp = time.mktime(datetime.strptime(date, '%Y-%m-%d').timetuple())
    if int(tstmp) > older:
        older = tstmp
        answer[0] = lst[0]

    if int(tstmp) < younger:
        younger = tstmp
        answer[1] = lst[0]

print(answer[0])
print(answer[1])