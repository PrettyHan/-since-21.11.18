# 팰린드롬인지 확인하기

words = input().lower()
type2 = ''
for word in words:
    type2 = word + type2

if words == type2:
    print('1')
else:
    print('0')       

    # for 문 돌리거나, reversed or reverse, [::-1]