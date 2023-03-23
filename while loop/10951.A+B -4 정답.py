# 10951번. A+B - 4 (정답)

# try except 사용하면 된다 ㅠㅠ

while True:
    try:
        A, B = map(int, input().split())
    except:
        break 
    print(A+B)
