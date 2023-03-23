# 2753번. 윤년

yun_year = input()
yun_year = int(yun_year)

if yun_year % 4 == 0 and yun_year % 100 != 0 or yun_year % 400 == 0:
    print("1")
else:
    print("0")

# if 
# 4 의 배수 일 때 나머지는 0
# 0 이 아니면 100의 배수가 아님
# 0 이면 400의 배수