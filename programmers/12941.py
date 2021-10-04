def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        print(A[i],B[i])
        answer += (A[i]*B[i])
    return answer