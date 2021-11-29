# 1110번. 더하기 사이클

A = int(input()) 

A_NUM = A

cycle = 0 # 길이 물어보는거라 길이 변수 지정

while True:
    sum = (A_NUM // 10) + (A_NUM % 10) # 각 자리 더 해주자
    new =  ((A_NUM % 10) * 10) + (sum % 10) # 새로운 수
    cycle += 1 # < 카운트
    if new == A:  # 같으면 break
        break
    A_NUM = new   # 새로운수를 A_NUM 에 넣어줌

print(cycle)        




# A % 10 = 1의자리
# (A - A//10) / 10 = 10의자리
# (A // 10) + ((A - A // 10) / 10) = 1 하고 10의 자리 더한 수