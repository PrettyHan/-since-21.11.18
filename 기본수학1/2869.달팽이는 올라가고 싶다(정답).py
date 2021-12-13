# 2869. 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())

day = 0
if (V - B) % (A - B) != 0: # 하루에 올라가는 거리 (A - B) , 목표지점 거리 (V - B)
    day = ((V - B) // (A - B)) + 1 # 나머지가 0 이 아니면 하루 더 올라갈 시간이 필요함
else:
    day = ((V - B) // (A - B)) # 나머지가 0 이면 그대로 프린트
print(day)