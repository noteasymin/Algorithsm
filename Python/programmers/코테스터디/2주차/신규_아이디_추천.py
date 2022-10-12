def solution(new_id):
    #1
    new_id = list(new_id.lower())
    new_lst = []
    chk_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','_','.']

    #2
    for i in new_id:
        if i in chk_lst:
            new_lst.append(i)

    #3
    cnt = 0
    if '.' not in new_lst:
        pass
    elif len(new_lst) < 2:
        pass
    else:
        while cnt != len(new_lst):
            if new_lst[cnt] == '.':
                if cnt == len(new_lst) - 1:
                    if new_lst[0] == '.':
                        del new_lst[0]
                        break
                elif new_lst[cnt+1] == '.':
                    del new_lst[cnt]
                    cnt = 0
                    continue
            cnt += 1


    #4
    if len(new_lst) > 0:
        if new_lst[0] == '.':
            del new_lst[0]

    if len(new_lst) > 0:
        if new_lst[len(new_lst)-1] == '.':
            del new_lst[len(new_lst)-1]


    #5
    if len(new_lst) == 0:
        new_lst.append('a')

    #6
    if len(new_lst) > 15:
        del new_lst[15:]

    if new_lst[len(new_lst)-1] == '.':
        del new_lst[len(new_lst)-1]

    #7
    if len(new_lst) < 3:
        while len(new_lst) != 3:
            new_lst.append(new_lst[len(new_lst)-1])


    new_lst = ''.join(new_lst)
    print(new_lst)
    return new_lst

new_id = "z-+.^."

solution(new_id)