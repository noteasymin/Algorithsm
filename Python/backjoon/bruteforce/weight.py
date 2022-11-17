def weight():
    c = int(input())
    rank = 1
    same = 1
    cnt = 0
    students = []
    for i in range(c):
        students.append(list(map(int,input().split())))
    
    students_array = sorted(students,reverse=True)
    

    for i in range(c):
        cnt += 1
        if i == 0:
            students_array[0].append(rank)
        elif students_array[i-1][0] == students_array[i][0] and students_array[i-1][1] == students_array[i][1]:
            rank = rank + 1
            students_array[i].append(cnt)
            same += 1
        elif students_array[i-1][0] > students_array[i][0] and students_array[i-1][1] > students_array[i][1]:
            rank = rank + 1
            students_array[i].append(cnt)
            same += 1
        elif students_array[i-1][0] < students_array[i][0] or students_array[i-1][1] < students_array[i][1]:
            students_array[i].append(same)

    for i in range(c):
        j = students_array.index(students[i])
        print(students_array[j][2],end = " ")
        

weight()