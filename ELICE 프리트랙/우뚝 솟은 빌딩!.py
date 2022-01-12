N = int(input())

for i in range(N):
    if i == 0:
        print('*')
    if i == 1:
        print('**')
    if i == 2:
        print('***')
    if i == 3:    
        print('****')
    elif i >= 4:
        print('*****')