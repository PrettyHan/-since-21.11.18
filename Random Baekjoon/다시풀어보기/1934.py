# 최소공배수
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    num1 = A
    num2 = B
    while num1 % num2 !=0: # 나누어 떨어질때까지 반복
        num1, num2 = num2, num1 % num2 # num1%num2 의 나머지와 작은수 num2 를 계속 나머지 해줌

    print(int((A*B)/num2))    # 실수로 변환되서 int 형으로 바꿔줌 