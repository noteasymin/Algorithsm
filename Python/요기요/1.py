# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10

    answer = []

    while stack1 or stack2 or stack3:
        temp = []
        if stack1:
            temp.append(stack1[-1])

        if stack2:
            temp.append(stack2[-1])

        if stack3:
            temp.append(stack3[-1])

        if stack1:
            if max(temp) == stack1[-1]:
                stack1.pop()
                answer.append('1')
                continue
        if stack2:
            if max(temp) == stack2[-1]:
                stack2.pop()
                answer.append('2')
                continue
        if stack3:
            if max(temp) == stack3[-1]:
                stack3.pop()
                answer.append('3')
                continue

    result = ''.join(answer)
    print(result)

stack1 = [2,7]
stack2 = [4,5]
stack3 = [1]
solution(stack1, stack2, stack3)