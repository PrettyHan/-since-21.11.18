# 11021번. A+B-7
T = int(input())

K = 0

for _ in range(T):
    A, B = map(int, input().split())
    K += 1
    print(f"Case #{K}: {A+B}")

