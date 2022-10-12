lst = []
def jump(current,battery,N):
    global lst
    if current == N:
        lst.append(battery)
        return lst

    if current == 0:
        current += 1
        battery += 1
        jump(current, battery, N)
        return lst

    if current * 2 > N:
        current += 1
        jump(current, battery, N)
        return lst

    if current * 2 <= N:
        current *= 2
        jump(current, battery, N)
        return lst
def solution(n):
    answer = 0

    while n != 0:
        if n == 2:
            break

        elif n % 2 == 0:
            n = n // 2

        else:
            answer += 1
            n = n // 2
    answer += 1

    print(answer)
solution(5)