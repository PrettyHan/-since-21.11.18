# 2884. 알람 시계
A = 45
H, M = map(int, input().split())

if M<45:
    ans_H = H-1 
    ans_M = (60+M)-A
elif M>=45:
    ans_H = H
    ans_M = M-45

if ans_H < 0:
    ans_H += 24

print(ans_H, ans_M)            