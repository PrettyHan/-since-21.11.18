# 3052번. 나머지

count = 0
num = []

for i in range(10):
    N = int(input())
    num.append(N%42)

    if num:
     count += 1  #.... 어떻게 count? 중복처리 어떻게해!!!!!!

print(count)     
