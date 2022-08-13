input_list = []


for i in range((int(input()))):
    input_list.append((int(input())))

def solve(input_list):
    print(round(sum(input_list) / len(input_list)))
    mid = len(input_list) // 2
    print(input_list[mid])
    
solve(input_list)