# 1002 . 터렛
# 조규현의 좌표 x1 y1 조규현-류재명 거리 r1
# 백승환의 좌표 x2 y2 백승환-류재명 거리 r2
# 류재명이 있을 수 있는 좌표의 수 = 원과 원의 접점의 개수


for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    R = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 # 두 원의 중점 거리
    if R == 0: # 두 원의 중점이 같을 때
        if r1 == r2: # 두원이 완전 똑같음
            print(-1)
        elif r1 != r2: # 도너츠
            print(0)
    else: # 두 원의 중점이 다를 때
        if R == r1+r2 or R == abs(r1-r2): # 두 원이 한점 겹침
            print(1)
        elif R > abs(r1-r2) and R < r1+r2: # 두 원이 두점 겹침
            print(2)
        else:
            print(0)                   
