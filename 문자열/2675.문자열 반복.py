# 2675번. 문자열 반복

T = int(input())

S = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"\"","$","%",'*','+','-','.','/',':']

for _ in range(T):
    X, Z = input().split()
    for word in Z:
        if word in S:
            print(word*int(X), end = '')

# 이거 왜 틀리지?