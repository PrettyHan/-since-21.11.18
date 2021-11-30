# 10818번. 최소, 최대

N = int(input())
num = list(map(int, input().split()))
max = num[0]
min = num[0]

for i in num[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i    

print(min, max)

# or

# num = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
 
# print(num_list[0], num_list[num-1])