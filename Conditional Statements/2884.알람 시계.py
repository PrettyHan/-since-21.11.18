# 2884번. 알람 시계
H, M = input().split()
H = int(H)
M = int(M)

if H <= 0 and M - 45 < 0:
    print(H -1 + 24, M - 45 + 60 )

elif H >= 0 and M - 45 > 0:
    print(H, M - 45)

else:
    print(H - 1, M - 45 + 60)

# 이게 맞나...?

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60
print(H, M - 45)

# 정답 ㅠㅠ
    