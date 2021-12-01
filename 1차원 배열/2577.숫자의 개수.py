# 2577번. 숫자의 개수
abc = []

A = int(input())
B = int(input())
C = int(input())

abc = str(A * B * C) # list 랑 str 넣어줘야 count 가능

for i in range(10): # 0 ~ 9 까지
    print(abc.count(str(i))) # 몇개인지 count


# abc.count("0")
# abc.count("1")
# abc.count("2")
# abc.count("3")  => for in