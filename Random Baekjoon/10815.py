# 10815

import sys

n = int(sys.stdin.readline()) # 5
n_list = list(map(int, sys.stdin.readline().split())) # 6 3 2 10 - 10
chack_num = int(sys.stdin.readline()) # 8
chack_list = list(map(int, sys.stdin.readline().split())) # 10 9 -5 2 3 4 5 -10
answer_list = []

for i in chack_list:
    if i in n_list:
        answer_list.append(1)
    else:
        answer_list.append(0)

print(answer_list)