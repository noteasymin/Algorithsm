import sys
from collections import deque


def solution():
    n, m = map(int, input().split())
    room_name = []

    time_table = deque(deque(0 for i in range(24)) for j in range(n))

    for i in range(n):
        room_name.append(input())
        time_table[i].appendleft(room_name[-1])

    for _ in range(m):
        room, start, end = map(str, input().split())
        room_index = room_name.index(room)
        for i in range(int(start) + 1, int(end) + 2):
            time_table[room_index][i] = 1

    new_time_table = sorted(time_table, key=lambda x: x[0])

    for i in new_time_table:
        print(i)

    for i in new_time_table:
        print(f'Room {i[0]}:')
        time = []
        answer = deque()

        for j in range(10, 20):
            if i[j] == 0:
                time.append(j-1)
                continue

            elif len(time) != 0:
                answer.append(time[0])
                answer.append(time[-1])
                time = []

        print(answer)

solution()
