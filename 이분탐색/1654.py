# 랜선 자르기 # 이분탐색
# K = 갖고있는 랜선의 개수
# N = 필요한 랜선의 개수

K, N = map(int, input().split()) # 4, 11
k_list = [] # 802 743 457 539

for i in range(K):
    k_length = int(input())
    k_list.append(k_length)

length_min = 1 # 최소 랜선 길이
length_max = max(k_list) # 최대 랜선 길이 # 802
ans = 0

while(length_min <= length_max): #
    mid = (length_min + length_max) // 2 # 소수점 버리기위해 몫으로 나누어서 중간값 설정
    count = 0 # 자른 횟수 카운팅
    for i in k_list:
        count += i //mid
    
    if count < N: 
        length_max = mid - 1
    
    elif count >= N:
        length_min = mid + 1
        ans = mid

print(ans)        



