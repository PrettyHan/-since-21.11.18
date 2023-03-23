# 1978번 문제
N = input()
ans_list = []
a = list(map(int, input().split()))
b = 2
for i in range(int(N)):
    if a[i]%b != 0:
        ans_list.append(a[i])
        b = 2
    else:
        b += 1

if 1 in ans_list :
    print(len(ans_list) - 1)
else:
    print(len(ans_list))
