# 4673번 셀프 넘버(정답)
self_list = list(range(1, 10001)) # 1 ~ 10000 까지의 리스트 만들어 줌
remove_list = [] # 생성자 지워야 되니까 생성자 들어갈 리스트

for self in self_list:
    for s in str(self): # str 로 "" 각 자릿수 분리
            self += int(s) # self 안에 생성자 넣어줌 그다음 int 로 정수로 돌려줌
    if self <= 10000: # 1만 이하의 생성자 이면
            remove_list.append(self) # remove_list에 넣어준다 

for remove_num in set(remove_list): # set으로 중복된 값 없애줌
        self_list.remove(remove_num) # self_list 에서 중복을 없앤 생성자들을 제거 해준다.
for self_num in self_list: # 생성자가 없는 셀프넘버들을 하나씩 print 해 주면 끝.
        print(self_num)    

    # 개어렵네 ;
