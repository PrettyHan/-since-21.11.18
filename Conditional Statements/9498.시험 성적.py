# 9498번. 시험 성적

test_result = input()
test_result = int(test_result) # 0~100점 이라는 범위 설정 

test_result >= 0
test_result <= 100


if test_result >= 90:
    print("A")
elif test_result >= 80 and test_result <= 89:
    print("B")
elif test_result >= 70 and test_result <= 79:
    print("C")
elif test_result >= 60 and test_result <= 69:
    print("D")
else:
     print("F")        
