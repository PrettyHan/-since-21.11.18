# 2292.벌집

N = int(input())
distance = 1 # 기본이동 1
A = 1 # 기본 벌집갯수범위 1
while N > A: # N 벌집이 A 벌집 갯수범위 안에 있을 때 까지 반복
    distance += 1 # 6의 배수 반복, 범위 안에 없으면 거리 1씩 증가
    A += 6 * distance # A범위 는 이동거리 1당 6의 배수
print(distance)    