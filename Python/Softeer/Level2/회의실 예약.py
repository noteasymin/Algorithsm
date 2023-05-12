import sys
from collections import deque


def solution():
    n, m = map(int, input().split())
    room_name = []
    cnt = 0

    time_table = deque(deque(0 for i in range(24)) for j in range(n))

    for i in range(n):
        room_name.append(input())
        time_table[i].appendleft(room_name[-1])

    for _ in range(m):
        room, start, end = map(str, input().split())
        room_index = room_name.index(room)
        for i in range(int(start) + 1, int(end) + 1):
            time_table[room_index][i] = 1

    new_time_table = sorted(time_table, key=lambda x: x[0])

    for i in new_time_table:
        cnt += 1
        print(f'Room {i[0]}:')
        time = []
        answer = deque()

        for j in range(10, 20):
            if (j == 19) & (len(time) != 0):
                answer.append(time[0] - 1)
                answer.append(time[-1])

            elif i[j] == 0:
                time.append(j)
                continue

            elif len(time) != 0:
                answer.append(time[0] - 1)
                answer.append(time[-1])
                time = []

        if len(answer) == 0:
            print('Not available')
            print('-----')
        elif len(new_time_table) != cnt:
            print(f'{len(answer) // 2} available:')
            for k in range(len(answer) // 2):
                print(f'{str(answer.popleft()).zfill(2)}-{str(answer.popleft()).zfill(2)}')
            print('-----')

        else:
            print(f'{len(answer) // 2} available:')
            for k in range(len(answer) // 2):
                print(f'{str(answer.popleft()).zfill(2)}-{str(answer.popleft()).zfill(2)}')


solution()
