def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    name = {}
    result = []
    for i in range(len(names_one)):
        name[names_one[i]] = steps_one[i]

    if len(names_two) > 0:
        for i in range(len(names_two)):
            name[names_two[i]] += steps_two[i]

    if len(names_three) > 0:
        for i in range(len(names_three)):
            name[names_three[i]] += steps_three[i]

    name = sorted(name.items(),key = lambda x:x[1],reverse = True)

    for i in name:
        result.append(i[0])

    print(result)

steps_one = [1,2,3]
names_one = ['james','bob','alice']
steps_two = [10,20,30]
names_two = ['james','alice','bob']
steps_three = [1000,1,1]
names_three = ['bob','alice','james']

solution(steps_one,names_one,steps_two,names_two,steps_three,names_three)