import datetime

date = input()

date = datetime.datetime.strptime(date, '%Y%m%d')

print(type(date))