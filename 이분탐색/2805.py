import sys
input = sys.stdin.readline

tree = 0
n, m = map(int, input().split())

heigh_list = list(map(int, input().split()))
cut_heigh = max(heigh_list)

while(tree < m):
    cut_heigh -= 1
    tree = 0
    for i in heigh_list:
        if(i - cut_heigh >= 0):
            tree += (i - cut_heigh)

print(cut_heigh)