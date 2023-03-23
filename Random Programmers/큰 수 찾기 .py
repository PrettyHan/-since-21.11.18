def solution(number, k): # 1924 , 2
    numlist = []
    for num in number: # 9 2 4 
        if not (numlist): # [9, 2]
            numlist.append(num) # 
            continue
        while k > 0 and numlist[-1] < num and numlist: # K = 1 true , 9 < 2 flase , [9] true 
            numlist.pop() # []
            k -= 1 # 2 => 1
            if not numlist or k == 0:
                break
        numlist.append(num)

    return ''.join(numlist)

print(solution('1924', 2))

# def solution(number, k):
#     answer = [] # Stack
    
#     for num in number:
#         while k > 0 and answer and answer[-1] < num:
#             answer.pop()
#             k -= 1
#         answer.append(num)
        
#     return ''.join(answer[:len(answer) - k])