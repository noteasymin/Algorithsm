def solution(s):
    answer = ''
    prev_char = ' '  # 이전 문자 초기화

    for char in s:
        if prev_char == ' ':
            answer += char.upper()  # 단어의 첫 문자이므로 대문자로 변환
        else:
            answer += char.lower()  # 단어의 나머지 문자는 소문자로 변환

        prev_char = char  # 이전 문자 업데이트

    return answer