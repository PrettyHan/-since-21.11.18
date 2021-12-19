# 소인수분해
N = int(input())
A = 2
while N != 1: # N이 1되면 멈춤 (몫이 1 ) 
    if N%A == 0: # N이 2 로 나누어 떨어지면 실행
        print(A) # A를 출력
        N = N//A   # N은 N//A 로 치환
    else:
        A += 1  # 해당하지않으면 3부터 다시 