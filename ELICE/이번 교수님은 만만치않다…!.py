lang = int(input())
think = int(input())
write = int(input())

test_list = [lang, think, write]

test_list.sort()
if test_list[0] >= 75 and think > 50:
    print('A+')
elif test_list[0] >= 50 and think > 50:
    print('A')
elif think < 50:
    print('F')
else:
    print('B+')