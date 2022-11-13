name = str(input())
count = 0
count2 = 1
answer = -1
dict_word = "ABCDEFGHIJKLM"
dict_word2 = "ZYXWVUTSRQPON"
dict = {}
dict2 = {}

for word in dict_word:
    dict[word] = count
    count += 1
for word2 in dict_word2:
    dict2[word2] = count2
    count2 += 1
    
print(dict, dict2)
for i in name:
    if i in dict:
        answer += dict[i]
        answer += 1
    if i in dict2:
        answer += dict2[i]
        answer += 1

print(answer)