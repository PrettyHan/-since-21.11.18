# 4344번. 평균은 넘겠지

C = int(input())

for _ in range(C):
    test = list(map(int, input().split()))
    
    test_avg = sum(test[1:])/test[0] # 평균값
    
    upper = 0 # 평균을 상회하는 인원 수
    
    for score in test[1:]: # test 점수들을 각 score 로 반복
        if score > test_avg: # 만약 평균점수보다 높은 점수가 있으면
            upper += 1 # 평균을 상회하는 인원수 += 1
    
    upper_avg = upper / test[0] * 100 # 평균을 상회하는 인원수 / 테스트 인원수
    
    print(f'{upper_avg:.3f}''%') # :3.f 로 소수점 3개까지 표기

    # % 안 넣어줘서 틀림 ㅡㅡ

