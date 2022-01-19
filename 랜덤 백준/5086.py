# 배수와 약수

a = 1
b = 1
while a and b != 0:
    a, b = map(int, input().split())
    if a and b == 0:
        break
    if b > a:
        if b % a == 0:
            print('factor')
        else:
            print('neither')      
    if a > b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')        