import sys
T = int(sys.stdin.readline())

def hello(n):
    count = 0
    if n == 1:
        count = 1
    elif n == 2:
        count = 2
    elif n == 3:
        count = 4
    else:
        count = hello(n-3) + hello(n-2) + hello(n-1)
    return count


for i in range(T):
    n = int(sys.stdin.readline())
    print(hello(n))