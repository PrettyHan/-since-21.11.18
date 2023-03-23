# 1065번.한수(다른방식)

def solve(n):
    a = []

    if n < 100:
        return True
    
    elif n < 1000 :
        while n != 0:    
            a.append(int(n % 10))
            n = n/10

        if (a[0] - a[1]) == (a[1] - a[2]):
            return True
        else:
            return False
    else:
        return False
    
    
N = int(input())
sum = 0

for i in range(1, N+1):
    if(solve(i) == True):
        sum += 1

print(sum)