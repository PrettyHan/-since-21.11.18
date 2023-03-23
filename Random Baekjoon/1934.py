# 최소공배수
T = int(input())

def mini(a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        if a%b == 0:
            return b
        else:
            return mini(a, a%b)        