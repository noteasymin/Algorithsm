lst = ['1 1 50', '1 1 95']

for i in lst:
    for j in lst:
        if i == j:
            continue
        elif i.split()[0] == j.split()[0] and i.split()[1] == j.split()[1] and i.split()[2] != j.split()[2]:
            if i.split()[2] > j.split()[2]:
                lst.remove(j)
            else:
                lst.remove(i)

for i in lst:
    i.replace('','\"')