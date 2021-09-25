def solution(s):
    answer = ''
    arr = list(s.lower())
    str =""
    flag = True
    for i in range(len(arr)):
        if flag and arr[i] != " " :
            answer = answer + arr[i].upper()
            flag = False
        elif arr[i] == " ":
            answer = answer + arr[i]
            flag = True
        else:
            answer = answer + arr[i].lower()
    return answer