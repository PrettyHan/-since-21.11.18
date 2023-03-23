# 비밀번호를 만들어주는 함수 yoonHa()를 만들어봅시다.
def yoonHa(nums):
    final = ''
    nums = int(nums)
    password = {4 : "love", 8 : "smile", 6 : "kiss"}

    for i in str(nums):
        i = int(i)
        final += password[i]
    return final
        
        

# 채점을 위한 코드입니다. 이를 수정하지 마세요!
nums = input()
print(yoonHa(nums))