# 1712번. 손기분익점

A, B, C = map(int, input().split())
if B < C:
    cnt = A / (C-B) # 고정비용 / (상품가격-가변비용) = 순익분기점
    cnt += 1
    print(int(cnt))
else:
    print(-1)    
