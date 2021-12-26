words = input()

for i in range(len(words)):
    if words[i] == words[-i]:
        print('1')
    else:
        print('2')    

 