def solution(flowers):
    lst = [0 for i in range(366)]

    for i in flowers:
        for j in range(i[0], i[1]):
            lst[j] += 1

    a = {0}

    result = [i for i in lst if i not in a]
    print(len(result))

flowers = [[2,5],[3,7],[10,11]]
solution(flowers)