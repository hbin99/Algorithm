def solution(table, languages, preference):
    answer = ''
    max = 0

    for i in range(5):
        score = 0
        sum = table[i].split(" ")
        for j in range(len(languages)):
            for k in range(1, 6):
                if languages[j] == sum[k]:
                    # print(languages[j])
                    score = score + ((6 - k) * preference[j])

        if max < score:
            max = score
            answer = sum[0]
        elif max == score:
            if answer > sum[0]:
                max = score
                answer = sum[0]
    return answer