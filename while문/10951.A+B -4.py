# 10951번. A+B - 4


banbok = 0 # 5번 반복하면 되나?

while banbok < 5:
    banbok += 1
    A, B = map(int, input().split())
    print(A+B)
