# 3052. 나머지(정답)

# set함수를 이용하면 된다..

count = [] # 리스트형

for i in range(10): 
    N = int(input()) # 10번 입력
    count.append(N%42) # 10번 입력한 N % 42
    
counts = set(count) # count 안의 수를 set 해서 중복처리

print(len(counts))  # len 으로 길이 구하면 끝!   