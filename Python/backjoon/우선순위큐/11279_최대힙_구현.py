import sys

input = sys.stdin.readline

heap = [0]
capacity = 0


def push(heap, n):
    global capacity
    # heap의 자리가 부족할 경우 배열을 2배로 늘려나간다.
    if len(heap) - 1 == capacity:
        heap = heap + [0] * len(heap)

    capacity += 1
    heap[capacity] = n

    # above heapify
    tn = capacity
    while (tn > 1):
        if heap[tn] > heap[tn // 2]:
            temp = heap[tn]
            heap[tn] = heap[tn // 2]
            heap[tn // 2] = temp
            tn //= 2
        else:
            break
    return heap


def pop(heap):
    global capacity
    if capacity == 0:
        return 0
    p = heap[1]
    heap[1] = heap[capacity]
    heap[capacity] = 0

    # below heapify
    tn = 1
    while (capacity > tn * 2):
        if heap[tn * 2] == 0 and heap[tn * 2 + 1] == 0:
            break
        if heap[tn] < max(heap[tn * 2], heap[tn * 2 + 1]):
            temp = heap[tn]
            if heap[tn * 2] > heap[tn * 2 + 1]:
                heap[tn] = heap[tn * 2]
                heap[tn * 2] = temp
                tn *= 2
            else:
                heap[tn] = heap[tn * 2 + 1]
                heap[tn * 2 + 1] = temp
                tn = tn * 2 + 1
        else:
            break
    capacity -= 1
    return p


for i in range(int(input())):
    x = int(input())
    if x:
        heap = push(heap, x)
    else:
        print(pop(heap))