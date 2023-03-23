price_list = {'아메리카노' : 4100, '카페라떼' : 4600, '카라멜마끼아또' : 5100}

N = int(input())
ans = 0
for i in range(N):
    order = str(input())
    ans += price_list[order]

print(ans)