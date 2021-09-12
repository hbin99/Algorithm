def solution(scores):
    answer = ''

    for i in range(len(scores)):
        temp = []
        for j in range(len(scores)):
            temp.append(scores[j][i])
            # print(temp)
        score = temp[i]
        # print(score)
        temp_max, temp_min = max(temp), min(temp)
        max_cnt, min_cnt = temp.count(temp_max), temp.count(temp_min)

        if (score == temp_max and max_cnt == 1) or (score == temp_min and min_cnt == 1):
            temp.remove(score)

        avg = sum(temp) / len(temp)

        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer