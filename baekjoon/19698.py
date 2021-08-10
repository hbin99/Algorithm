N,W,H,L = map(int,input().split())

A = W//L
B = H//L
if N < A * B:
    print(N)
else:
    print(A * B)