def solution(brown, yellow):
    w_lst = []
    for i in range(1, (brown+yellow) + 1):
        if (brown + yellow) % i == 0:
            w_lst.append(i)

    for w in w_lst:
        h = (brown + yellow) // w
        wh = []
        wh.append(w)
        wh.append(h)
        wh.sort(reverse=True)

        if (wh[0] * 2) + (wh[1] * 2 - 4) == brown:
            return wh

brown = 10
yellow = 2
solution(brown, yellow)
