hour, min = map(int, input().split())
time = int(input())
ans_min = 0
ans_hour = 0

ans_hour = hour + (time)//60
ans_min = min + (time%60)
if ans_min == 60:
    ans_hour += 1
    ans_min -= 60

if ans_hour < 24:
    print(ans_hour, abs(ans_min))
else:
    print(ans_hour - 24, abs(ans_min))