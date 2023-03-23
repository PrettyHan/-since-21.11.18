# 0 = not cute / 1 = cute
N = int(input())
B = []
for i in range(N):
    A = int(input())
    B.append(A)
if B.count(0) > B.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")