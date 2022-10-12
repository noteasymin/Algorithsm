a = int(input())
number = []
for x in range(a):
  check = 0
  for y in range(len(str(x))):
    check += int(str(x)[y])
    if a == check + x:
      number.append(x)

if len(number) == 0:
  print(0)
else: print(min(number))