from collections import deque
from itertools import combinations

def solution(orders,course):
    global answer
    global course_lst

    answer = deque()
    course_lst = {}

    for i in orders:
        add_menu(sorted(i))

    global answer_lst
    answer_lst = list(course_lst.items())

    for i in course:
        check_len(i)

    new_answer = []

    for i in list(answer):
        d = ''.join(i)
        new_answer.append(d)

    print(sorted(new_answer))

def add_menu(orders):
    for i in range(2, len(orders)+1):

        lst = list(combinations(orders, i))

        for j in lst:
            if j not in course_lst:
                course_lst[j] = 1
            else:
                course_lst[j] += 1

def check_len(course):
    temp = []
    max_num = 2
    for i in answer_lst:
        if course == len(i[0]):
            if i[1] > max_num:
                if i[0] not in temp:
                    temp = []
                    max_num = i[1]
                    temp.append(i)
            elif i[1] == max_num:
                if i[0] not in temp:
                    max_num = i[1]
                    temp.append(i)

    for i in temp:
        answer.append(i[0])



orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

solution(orders,course)

