from collections import Counter

# 문자열
data = Counter('hello wolrd')
print(data)

# 리스트
data = Counter(['1', '2', '2', '3', '3', '3'])
print(data)         # 등장횟수가 많은 데이터부터 출력
print(data.keys())