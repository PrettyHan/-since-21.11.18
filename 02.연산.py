# 1. 비교 연산 (중요!!)
# 결과가 불린형으로 
print(2 > 3) # False
print(15 < 30) # True
print(1.5 >= 0) # True
print(3 <= 3) # True
print("팙팙팙" == "팙팗팙") # False
print("1111111111111111111" != "11111111111111111111") # True # != < 다르나요?

# 2. 논리연산
print("- 논리연산 문제")
print(4 < 6 and 10 >= 10) # True and True -> True
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다" == "나는 할 수 있다") # False and True -> True
print(not 5==5) # not True -> False

# 3. 멤버쉽 연산
print("- 멤버쉽 문제")
print("a" in "abc") # 포함되어 있다면 True
print("d" not in "abc") # 포함되어 있지 않다면 True

# 4. 