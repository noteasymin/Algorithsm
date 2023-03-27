def solution(invitationPairs):
    result = {}
    new_result = {}
    invited = []
    invitedinvited = []
    for i in invitationPairs:
        if i[0] in invited:
            invitedinvited.append(i[1])
        else:
            invited.append(i[1])


    for i in invitationPairs:
        result[i[0]] = 0
        result[i[1]] = 0
        new_result[i[0]] = 0
        new_result[i[1]] = 0


    for i in invitationPairs:
        result[i[0]] += 1
        if i[1] not in invited:
            pass
        if i[1] in invited:
            new_result[i[0]] += invited[i[1]] * 10

        if i[1] in invitedinvited:
            new_result[i[0]] += invitedinvited

    print(invited)
    print(invitedinvited)
    print(result)


invitationPairs = [[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]

solution(invitationPairs)