# 1546번. 평균

N = int(input()) # 과목 수

test = list(map(int, input().split())) # 테스트 리스트형으로 input

max_score = max(test) # max 값 설정해주고

new_list = [] # 조작 점수 담을 리스트 

for score in test: # test 안에 있는 각 score 조작
    new_list.append(score/max_score*100) # 조작 과정

new_avg = sum(new_list)/N # 평균 = SUM / N

print(new_avg)

