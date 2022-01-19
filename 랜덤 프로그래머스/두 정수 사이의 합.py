
def solution(a, b):
    ans = 0
    if a > b:
        up, down = a, b
    else:
        up, down = b, a
    for i in range(down, up+1):
        ans += i
    return ans

print(solution(4, 2))    