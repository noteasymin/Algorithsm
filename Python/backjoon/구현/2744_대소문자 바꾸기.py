s = input()
new_s = []
for i in s:
    if i.islower():
        new_s.append(i.upper())
    else:
        new_s.append(i.lower())

print(''.join(new_s))