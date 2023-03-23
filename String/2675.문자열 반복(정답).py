# 2675번. 문자열 반복

T = int(input())

for _ in range(T):
    X, Z = input().split()
    for word in Z:
         print(word*int(X),end ='')
    print() # 줄넘김 와 이런방법이;;      

# S 범위 와 조건문 없애버림