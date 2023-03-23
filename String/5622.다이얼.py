# 5622번. 다이얼

x = input().lower()
cnt = 0
for i in x:
    if i == 'a' or i == 'b' or i == 'c':
        cnt += 3
    elif i == 'd' or i == 'e' or i == 'f':
        cnt += 4
    elif i == 'g' or i == 'h' or i == 'i':
        cnt += 5
    elif i == i == 'j' or i == 'k' or i =='l':
        cnt += 6
    elif i == i =='m' or i =='n' or i =='o':
        cnt += 7
    elif i == 'p' or i =='q' or i =='r' or i =='s':
        cnt += 8
    elif i == 't' or i =='u' or i =='v':
        cnt += 9
    elif i == 'w' or i =='x' or i =='y' or i =='z':
        cnt += 10
    else:
        cnt += 0
print(cnt)

# ;; 너무길지않나

# 다른 방법 

x = input() # if X = ABC
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt = 0
for i in range(len(x)): # x의 길이 만큼 반복 i = 0,1,2
    for j in dial: # J = 각 문자열 
        if x[i] in j: # X[0,1,2] = 'A','B','C' in 각 문자열에 있으면
            cnt += dial.index(j)+3 # index 숫자 + 3 해서 올라감
print(cnt)  # 천잰가?