a, b, c = map(int, input().split())
A = []
A.append(a)
A.append(b)
A.append(c)
A.sort()
B = list(set(A))
if len(B) == 1: # 모두가 같음
    print(10000+B[0]*1000)
elif len(B) == 3: # 3개가 다 다름
    print(B[-1]*100)
else: # 2개 만 같음
    print(1000+A[1]*100) # set 되기 때문에 A 리스트 불러와야 됨
