# 주사위 게임
T = int(input())
ans = []

for i in range(T):
    a, b, c = map(int, input().split())
    A = 0
    B = 0
    C = 0
    if a == b == c:
        A = (10000+a*1000)
    elif a == b:
        B = (1000+a*100)
    elif a == c:
        B = (1000+a*100)
    elif c == b:
        B = (1000+c*100)
    else:
        C = max(a,b,c)*100
    ans.append(max(A, B, C))

ans.sort()
print(ans[-1])
