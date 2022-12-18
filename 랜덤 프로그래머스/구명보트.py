def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1
    arr = sorted(people)
    # 	[50, 50, 70, 80]
    while start <= end:
        if arr[start] + arr[end] <= limit:
            start += 1
            end -= 1
        else: # 가장 무거운사람 혼자타고 가~
            end -= 1
        answer += 1

    return answer