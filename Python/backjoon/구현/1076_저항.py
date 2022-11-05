dic1 = {'black': 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}
dic2 = {'black': 1, 'brown' : 10, 'red' : 100, 'orange' : 1000, 'yellow' : 10000, 'green' : 100000, 'blue' : 10**6, 'violet' : 10**7, 'grey' : 10**8, 'white' : 10**9}
answer = []
for i in range(2):
    s = input()
    answer.append(str(dic1[s]))

s = input()
answer = int(''.join(answer)) * dic2[s]

print(answer)