# 2869. 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())

upup = 0 
day = 0
down = 0
updown = 0
while True:
    if updown >= V:
        break
    if day >= 1:
        down += B
    upup += A
    updown = upup-down
    day += 1
print(day)    # 시간초과 ㅜㅜㅜㅜㅜㅜㅜㅜㅜ