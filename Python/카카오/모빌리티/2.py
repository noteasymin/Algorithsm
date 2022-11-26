def solution(id_list, k):
    new_id = []
    for i in id_list:
        temp = i.split()
        for j in temp:
            if j not in new_id:
                new_id.append(j)

    dic = {}
    for i in new_id:
        dic[i] = 0

    for i in id_list:
        temp = i.split()
        temp = set(temp)
        for j in temp:
            if dic[j] < k:
                dic[j] += 1

    print(sum(dic.values()))


id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY",
"ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k = 3
solution(id_list,k)