# 네 번째 점
A = []
B = []

for i in range(3):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for ans in range(3):
    if A.count(A[ans]) == 1: # A[0,1,2] < 3개 다돌려서 count 1 된거 찾음
        ans1 = A[ans]
    if B.count(B[ans]) == 1:
        ans2 = B[ans]
print(ans1, ans2)         