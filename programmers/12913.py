def solution(land):
    answer = 0
    #print( land[1][0])
    print(len(land))
    for i in range(len(land)-1):
        #land[1][0] += max(land[0][1],land[0][2],land[0][3])
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][1],land[i][0],land[i][3])
        land[i+1][3] += max(land[i][1],land[i][2],land[i][0])
        print( land[i+1][0])
    answer = max(land[len(land)-1])
    return answer