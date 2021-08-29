def solution(s):
    answer = 0
    stext = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    sEng = ["0","1","2","3","4","5","6","7","8","9"]

    for i in range(len(stext)):
        s = s.replace(stext[i], str(i))

    answer = int(s)
    return answer