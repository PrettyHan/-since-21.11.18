# 1065번. 한수

N = int(input())
hansu = 0

for i in range(1, N+1): # range 함수로 1 ~ N+1 까지 한수 범위
    N_list = list(map(int, str(i))) # 자릿수 분할을 위한 list(str) and map함수로 int로 변환시켜줌
    if i < 100: # 100이하는 모두 한수
        hansu += 1
    elif N_list[0] - N_list[1] == N_list[1] - N_list[2]: # map(int, 리스트) 안해주면 리스트 계산 못함 # TypeError: unsupported operand type(s) for -: 'str' and 'str'
        hansu += 1

print(hansu)
