def hanoi(n, from_pos, to_pos, aux_pos,answer):

    if n == 1:
        print(from_pos, '->', to_pos)
        answer.append([from_pos,to_pos])
        return

    hanoi(n - 1, from_pos, aux_pos, to_pos,answer)
    answer.append([from_pos,to_pos])
    print(from_pos, '->', to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos,answer)

def solution(n):
    answer = []
    hanoi(n,1,3,2,answer)
    return answer

solution(3)