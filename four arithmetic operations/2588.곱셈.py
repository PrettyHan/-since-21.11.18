# 2588번. 곱셈
A = input()
B = input()

A = int(A)
B = int(B)

Sub1 = A*((B%100)%10)
Sub2 = A*((B%100)//10)
Sub3 = A*(B//100)
result = A*B


print(Sub1, Sub2, Sub3, result, sep='\n')





