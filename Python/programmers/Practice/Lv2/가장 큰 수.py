def solution(numbers):
    numbers = list(map(str, numbers))

    # 비교 함수를 lambda 함수로 정의하여 사용합니다.
    compare = lambda x: x * 3
    print(compare)
    numbers.sort(key=lambda x: compare(x), reverse=True)

    if numbers[0] == "0":
        return "0"

    print("".join(numbers))
    return "".join(numbers)


numbers = [6, 10, 2]
solution(numbers)
