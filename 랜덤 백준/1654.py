# 랜선 자르기 # 이분탐색
# K = 갖고있는 랜선의 개수
# N = 필요한 랜선의 개수
import sys


K, N = map(int, sys.stdin.readline().split()) # 4, 11
k_list = [] # 802 743 457 539

for i in range(K):  
    k_length = int(sys.stdin.readline())
    k_list.append(k_length)

length_min = 1 # 최소 랜선 길이
length_max = max(k_list) # 최대 랜선 길이 # 802
ans = 0

while(length_min <= length_max): #
    mid = (length_min + length_max) // 2 # 소수점 버리기위해 몫으로 나누어서 중간값 설정 # 대충 400
    count = 0 # 자른 횟수 카운팅

    for i in k_list:
        count += i // mid # 길이를 중간값으로 나누어 준 횟수
    
    if count < N: # 만드려는 갯수 N 보다 작다면 더 작은 값으로 나누어서 횟수를 늘려줌 mid -1
        length_max = mid - 1
    
    elif count >= N: # 만드려는 갯수 N 보다 크다면 더 큰 값으로 나누어서 횟수를 줄여줌 mid + 1
        length_min = mid + 1
    
    ans = length_max # while(length_min <= length_max) 을 벗어날 때 length_max

print(ans)        



