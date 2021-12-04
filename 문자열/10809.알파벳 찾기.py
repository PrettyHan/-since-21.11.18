# 10809번. 알파벳  찾기

S = input()

AB = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for ABCD in AB:
    print(S.find(ABCD), end = ' ')
    
