# 2908번. 상수

N, N2 = input().split()

A = N[::-1]
B = N2[::-1]

if A > B:
    print(A)
elif A < B:
    print(B)

    # [::-1] 역순