def solution(numbers):
    check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_of_not = 0

    for i in check:
        if i not in numbers:
            sum_of_not += i

    return sum_of_not