# 10250. ACM 호텔
T = input()
X = 0
Y = 0
for i in range(int(T)):
    H, W, N = map(int, input().split())
    X = N//H + 1
    Y = N % H
    if N % H == 0:
       X = N//H
       Y = H
    print(f'{Y*100+X}')