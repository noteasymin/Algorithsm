def solution(sizes):
    answer = 0

    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]

    max_w = sizes[0][0]
    max_h = sizes[0][1]

    for i in sizes:
        if max_w < i[0]:
            max_w = i[0]

        if max_h < i[1]:
            max_h = i[1]


    answer = max_w * max_h

    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

solution(sizes)