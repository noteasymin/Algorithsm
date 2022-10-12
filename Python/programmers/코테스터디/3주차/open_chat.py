dic = {}
result = []

def solution(record):
    for i in record:
        sol(i)

    for i in record:
        answer(i)

    return result


def sol(record):
    global dic
    record = record.split()
    if record[0] == 'Enter':
        dic[record[1]] = record[2]
    elif record[0] == 'Leave':
        pass
    else:
        dic[record[1]] = record[2]


def answer(record):
    global dic
    global result

    record = record.split()

    if record[0] == 'Enter':
        result.append(f'{dic[record[1]]}님이 들어왔습니다.')
    elif record[0] == 'Leave':
        result.append(f'{dic[record[1]]}님이 나갔습니다.')