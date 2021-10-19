def solution(n):
    answer = 0
    m = n
    cnt = bin(n).count('1')

    while True:
        m += 1
        if bin(m).count('1') == cnt:
            return m
    return m