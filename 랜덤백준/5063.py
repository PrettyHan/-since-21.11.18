# TGN
T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    if b - c > a:
        print("advertise")
    elif b - c == a:
        print("does not matter")
    else:
        print("do not advertise")