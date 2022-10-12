def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    c = sum(day[:a - 1]) + b

    c = c % 7 - 1

    print(date[c])
    return date[c]

solution(5, 24)