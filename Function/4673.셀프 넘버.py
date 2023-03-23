# 4673번. 셀프 넘버

def d(n):
    remove_list = 0
    for self_num in list(str(n)): # n을 제외한 각 자리 숫자 만들기 list(str(n))
        remove_list = remove_list + int(self_num) # 이전 생성자 + 각 자리 숫자 더하기
    return int(n) + remove_list # n 값도 더 해주고 리턴

remove_list = [] 

for i in range(1,10001): # 1~10000 까지의 생성자 리스트를
    f = d(i) 
    remove_list.append(f) # remove_list 에 넣어준다

answer = list(range(1, 10001)) # 1~ 10000 리스트 만들어 준다

real_answer = list(set(answer) - set(remove_list)) # 둘이 빼 줌

real_answer.sort() # 정렬

for ans in real_answer: # 하나씩 출력해야되니까 for in 해줌
    print(ans)

# 이것도 정답 