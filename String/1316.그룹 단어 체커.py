# 1316번. 그룹 단어 체커

N = int(input())
count = N # 단어 총 N개 중에

for _ in range(N): # 단어의 갯수 만큼 반복
    words = input().lower() # 혹시몰라 소문자 통일
    for word_len in range(len(words)-1): # 단어 갯수만큼 index 생성
        if words[word_len] != words[word_len+1]: # 다음 숫자와 그 전의 숫자가 다르고
            if words[word_len+1] in words[:word_len]: # 다음숫자가 나머지 숫자에 포함되어있으면 # word_len => 단어길이
                count -= 1 # 그룹 단어가 아니기 때문에 카운트 - 1
                break # break 해주고 다음 단어 조사

print(count)