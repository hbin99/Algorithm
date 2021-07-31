cnt = int(input())
if cnt == 0:
    print("divide by zero")
else:
    list = list(map(int, input().split()))
    av1 = sum(list)/cnt
    av2 = sum(list)/cnt
    result = av1 / av2
    print("%.2f" % result)