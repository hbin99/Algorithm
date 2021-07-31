# A = list(map(int,input().split())) #태어난 년 월 일 2003 3 5
# B = list(map(int,input().split()))  #기준 날짜 2003 4 5
#
# M = 0
# S = 1
# Y = 0
#
# if A[0] == B[0]:
#     M = 0
#     S = 1
#     Y = 0
# elif A[0] < B[0]:
#     if A[1] <= B[1]:
#         if A[2] <= B[2]:
#             M = B[0]-A[0]
#         else:
#             M = B[0] - A[0] - 1
#     elif B[0]-A[0] == 1:
#         M = 0 # 생일이 안지남
#     elif B[0]-A[0] > 1 and A[1] > B[1]:
#         M = B[0]-A[0] - 1
#     S = S + (B[0]-A[0])
#     Y = B[0]-A[0]
#
# print(M)
# print(S)
# print(Y)

a,b,c=map(int, input().split())
x,y,z=map(int, input().split())
if(x==a):#0살인가
    print(0)#만나이
    print(1)#세는나이
    print(0)#생년
elif(x>a):#한살 이상인가
    if(y>b):#생일인 달이 지났는가
        print(x-a)
        print(x-a+1)
        print(x-a)
    elif(y==b):#생일인 달인가
        if(z>=c):#생일인 날이 지났는가? 혹은 생일인가
            print(x-a)
            print(x-a+1)
            print(x-a)
        else:#생일인 날이 지나지 않음
            print(x-a-1)
            print(x-a+1)
            print(x-a)
    else:#생일 전임
        print(x-a-1)
        print(x-a+1)
        print(x-a)