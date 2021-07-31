list1 = [int(input()) for _ in range(3)]
list2 = [int(input()) for _ in range(3)]
A = list1[0]*3 + list1[1]*2 + list1[2]
B = list2[0]*3 + list2[1]*2 + list2[2]
if A == B:
    print("T")
elif A > B:
    print("A")
else:
    print("B")