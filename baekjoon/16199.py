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