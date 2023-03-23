# 2941번. 크로아티아 알파벳
# replace() 함수를 사용하면 된다

A = input().lower()
count = 0

words = ["c=","c-","dz=","d-","lj","nj","s=","z="]

# c= => *
# c- => * 등

for word in words:
    A = A.replace(word, '*') # words 안에있는 word를 한글자로 표현 그리고 길이를 재면 됨

print(len(A))