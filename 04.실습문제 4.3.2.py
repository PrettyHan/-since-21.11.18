# 실습문제 4.3.2
# 사용자로부터 태어난 연도를 입력 받고
# 현재 나이를 출력하기

year = input("태어난 연도를 입력하세용 >>") # or input 에 int 
age = 2021 - float(year) + 1
print("현재나이는", age, "세 입니다.")