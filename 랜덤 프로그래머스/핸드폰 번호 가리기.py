def solution(phone_number):
    a1 = phone_number[:-4]
    a2 = phone_number.replace(a1, "*" * len(a1))
    return a2