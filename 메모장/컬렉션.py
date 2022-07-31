from collections import Counter

# 문자열
data = Counter('hello wolrd')
print(data)

# 리스트
data = Counter(['1', '2', '2', '3', '3', '3'])
print(data)         # 등장횟수가 많은 데이터부터 출력
print(data['1'])
print(data['3'])
print(data['0'])    # 등장하지 않는 원소는 0 으로 출력
print(dict(data))   # 사전순으로 출력