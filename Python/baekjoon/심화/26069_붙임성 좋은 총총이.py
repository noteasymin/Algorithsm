def solution():
    n = int(input())
    dance = set()
    check = 0
    for i in range(n):

        human1, human2 = input().split()
        if human1 == 'ChongChong':
            dance.add(human2)
        elif human2 == 'ChongChong':
            dance.add(human1)

        if human1 in dance:
            dance.add(human2)
        elif human2 in dance:
            dance.add(human1)

    print(len(dance))


solution()
