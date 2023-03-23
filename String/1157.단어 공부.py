# 1157번. 단어 공부

alphabet = input().upper() # upper() : 문자열을 대문자로
alphabet_list = list(set(alphabet)) # set 해서 중복값 삭제

alpha = [alphabet.count(i) for i in alphabet_list] # 모든 문자열 카운트 = alpha

if alpha.count(max(alpha)) > 1:
    print('?')
else:
    print(alphabet_list[alpha.index(max(alpha))]) # alphabet_list 안에 있는 가장 많이 count 된 alpha 의 정보를 갖고옴

    # 못 품 ㅠㅠ

print(alpha)    