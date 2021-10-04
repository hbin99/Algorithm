def solution(n):
    answer = []

    for i in range(0, n + 1):
        if i == 0 or i == 1:
            answer.append(i)
        elif i >= 2:
            sum = answer[i - 1] + answer[i - 2]
            answer.append(sum % 1234567)

    return answer[n]