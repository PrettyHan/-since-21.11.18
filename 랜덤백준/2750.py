# 2750
T = int(input())
A = []
for i in range(T):
    N = int(input())
    A.append(N)
    A.sort()

for ans in A:
    print(ans)