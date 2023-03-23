# 1330번. 두 수 비교하기

x, y = input().split()   # split() 공백을 기준으로 나누어 줌

x = int(x)  # 너는 정수야~
y = int(y)  # 너는 정수야~

if x > y:
    print('>')
elif x < y:
    print('<')
else:
    print('==') 
