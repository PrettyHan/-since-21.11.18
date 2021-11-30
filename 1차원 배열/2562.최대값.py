# 2562번. 최대값
num_list = []

for _ in range(9):
    i = int(input())
    num_list.append(i)

num_list.sort()
max_num = num_list[-1]
index = num_list.index(max_num)

print(max_num)
print(index)

# 이거 왜 틀림..??


