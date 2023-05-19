from collections import Counter
lst = []
avg = 0
for i in range(10):
    lst.append(int(input()))
    avg += lst[-1]

lst = Counter(lst)
print(avg//10)
print(lst.most_common()[0][0])