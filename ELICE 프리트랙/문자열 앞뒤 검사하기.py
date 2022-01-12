A = str(input()).lower()

B = A[::-1]

for i in range(len(A)):
    if A[i] == B[i]:
        print('Same')
    else:
        print('Different')
    