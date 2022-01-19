H, M, S = map(int, input().split())

T = int(input())

S += T
M += S//60
H += M//60

S%=60
M%=60
H%=24

print(H, M, S)
