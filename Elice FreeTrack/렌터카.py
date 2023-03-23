# 지시사항 1~3번을 참고하여 코드를 작성하세요.
H = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 지시사항 4번을 참고하여 코드를 작성하세요.
result = 0

car1 = H*A

if H > C:
    car2 = B + (H-C) * D
elif H <= C:
    car2 = B
    
if car1 > car2:
    result = car2
elif car1 < car2:
    result = car1
elif car1 == car2:
    result = car1

# 아래 코드는 결과를 확인하기 위한 코드입니다.
print(result)