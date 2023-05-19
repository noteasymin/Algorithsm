import datetime

current = input().split(':')
time = input().split(':')

current = datetime.datetime(2020,1,1,int(current[0]),int(current[1]),int(current[2]))
time = datetime.datetime(2020,1,1,int(time[0]),int(time[1]),int(time[2]))

if current < time:
    if len(str(time-current)) != 8:
        print(str(time-current).rjust(8,'0'))
    else:
        print(time - current)
else:

    print(''.join(list(str(time - current))[8:]))