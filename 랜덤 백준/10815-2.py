# 10815-2 이분 탐색
# 상근이가 가지고있는 수[3,2,1,5,6] = n_list
# 상근이가 가지고있는 수와 일치 하는가? [1,3,2,4,5,6] = m_list
import sys
                # [1,3,2,4,5,6] [1,2,3,5,6]
def binary_search(element, some_list, start=0, end=None):
    if end == None: # 초기값 end 설정
        end = len(some_list) - 1   # 4 => index 최대번호
    if start > end: # 계속 돌렸는데도 값이 안나옴 return 0
        return 0

    mid = (start + end) // 2 # 0+4 => 1,2,3,5,6 [2] => 3

    if element == some_list[mid]: # 값이 일치하는 조건 찾음 return 1
        return 1
         # 1           # 2
    elif element < some_list[mid]: # [3 -> 2 -> 1]
        end = mid - 1
        # 4        #  3
    elif element > some_list[mid]: # [3 -> 5 -> 6]
        start = mid + 1
    
    return binary_search(element, some_list, start, end)

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(n_list)

answer_list = []
   # 0 1 2 3 4 5 6                 #6                    
for i in range(len(m_list)):
    answer_list.append(binary_search(m_list[i], sorted_list)) #

answer = " ".join(map(str, answer_list)) # 배열을 뛰어쓰기 넣고 합쳐줌
print(answer)