# 개표

pe = input()
po = input()
A = 0
B = 0
for i in po:
    if i == 'A':
        A += 1
    else:
        B += 1    
if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')