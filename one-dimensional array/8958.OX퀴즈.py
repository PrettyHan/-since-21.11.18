N = int(input())  # 반복 할 N 입력

for _ in range(N): # N 만큼 반복
    ox_list = list(input())  # ox_list 에 하나씩 oxoxo 넣어줌 
    score = 0 # o 의 점수
    sum_score = 0 
    for ox in ox_list: 
        if ox == 'O':
            score += 1
            sum_score = score+sum_score # 연속된 o의 점수 + o 의 점수
        else:
            score = 0
    print(sum_score)