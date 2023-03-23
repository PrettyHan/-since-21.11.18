def solution(s):
    ans = ""
    dict = "" # 키 값 넣어주기
    words = {
        "zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
        "six": '6', "seven": '7', "eight": '8', "nine": '9'
    }  # s가 문자열로 들어가기 때문에 숫자도 문자열로
    for s_word in s: # s 안에 있는 숫자 반복
        if s_word in '0123456789':
            ans += s_word
        else: # 문자 반복
            dict += s_word
            if dict in words.keys():
                ans += words[dict]
                dict = '' # 구별하기위해 묶어줘야댐
    return int(ans) # 숫자 변환

print(solution(input()))
