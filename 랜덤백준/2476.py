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
    ans.append(max(A, B, C)) # 3개 append 못하니까 차라리 max 함수로 a,b,c 나오는 숫자대로 갖고옴 B 되면 A, C 는 자동으로 0 되서 어챂 똑같음

ans.sort()
print(ans[-1])
