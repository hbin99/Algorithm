def solution(s):

    arr = list(map(int,s.split(" ")))
    print(arr)
    answer = str(min(arr)) + ' ' + str(max(arr))
    return answer