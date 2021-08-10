list = list(map(str,input().split()))

for i in range(len(list)):
    if list[i] == '+':
        a = int(list[i-1])
    elif list[i] == '=':
        b = int(list[i-1])
        c = int(list[i+1])

if a + b == c:
    print("YES")
else:
    print("NO")