import copy


def calc(check_cha):
    a = abs(ord('A') - ord(check_cha))
    b = abs(ord('Z') - ord(check_cha)+1)

    return min(a,b)

def solution(name):
    new_name = list(copy.deepcopy(name))
    if set(name) == {'A'}:
        return 0

    index_f = 0
    index_s = 0
    cnt = 0
    for i in name:
        if cnt == len(name) - 1:
            if name[cnt] == 'A':
                break
        if cnt == 0:
            index_f += calc(i)
            cnt += 1
        else:
            index_f += calc(i)
            index_f += 1

        del new_name[0]
        if set(new_name) == {'A'}:
            print(index_f)
            break
        print(index_f)

    cnt = 0
    new_name = list(copy.deepcopy(name))
    new_name.append(new_name[0])
    del new_name[0]

    for i in range(len(name)):
        print(name[cnt])
        if cnt == 0:
            index_s += calc(name[cnt])
            cnt = len(name) - 1

        else:
            index_s += calc(name[cnt])
            index_s += 1
            cnt -= 1

        print(new_name)
        del new_name[0]
        if set(new_name) == {'A'}:
            print(new_name)
            print(index_f,index_s)
            break

        print(index_s)



    print(min(index_f, index_s))

name = 'JEROEN'
solution(name)