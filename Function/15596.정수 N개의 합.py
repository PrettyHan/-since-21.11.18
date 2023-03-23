# 15596. 정수의 합

def solve(a):
    total = 0
    for x in range(0,a): # a => range(0,8) 반복문에서 a는 정수라 그대로 사용 불가
        total += x
    return total    

print(solve(8))


# or sum 으로 풀 수 있음

def solve(a):
    total = 0
    total = sum(a)
    return(total)