string = input("")

if string == " ": # 문장 자체가 공백인 경우 
    print(0)
else : 
    words = string.split(" ") # 띄어쓰기로 구분
    
    while '' in words : # 공백이 포함되어 있을경우 공백 삭제
        words.remove('')
        
print(len(words))

# split 함수 사용했으면 간단했다..