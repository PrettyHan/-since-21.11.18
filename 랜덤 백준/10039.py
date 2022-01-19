# 평균 점수
ans = 0
for x in range(5):
    a = int(input())
    if a < 40:
        ans += 40
    else:
        ans += a

print(int(ans/5))        
