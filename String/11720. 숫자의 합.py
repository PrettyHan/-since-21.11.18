# 11720번. 숫자의 합

N = input()

print(sum(map(int, input()))) # 각 자릿수 를 int로 변환 후 sum

# or 

N = input()

nums = input()
total = 0
for i in nums:
    total += int(i)

print(total)
