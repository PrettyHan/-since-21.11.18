# 수들의 합
S = int(input())
A = 0
for i in range(1,S+1):
    A += i
    if A > S:
        print(i-1)
        break