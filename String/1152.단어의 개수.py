alphabet = input("") # input 의 "" 넣어서 공백값 넣어줌 

alphabet_list = list(alphabet)

if alphabet_list[0] != ' ':
    count_list = alphabet_list.count(' ') + 1

else:
    count_list = alphabet_list.count(' ')

print(count_list)

# 왜 틀려!!!!!!!!!!!!!!!!!!!!!!