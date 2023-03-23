# 8393번. 합
n = int(input())

result = 0

for i in range(1, n+1): # 1~ n 까지 뽑아줌
    result += i   # 각 숫자 범위들을 더해준다
print(result)