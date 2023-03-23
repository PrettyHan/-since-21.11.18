import sys

input = sys.stdin.readline
n = int(input())
signal = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    send = signal[i] # [6 9 5 7 4]
    while stack:
        if send < stack[-1][1]: # 수신 가능
            answer[i] = stack[-1][0] + 1 # 인덱스
            break
        else: # 수신불가
            answer[i] = 0
            stack.pop()
    stack.append([i, send]) #([6, 0])

print(*answer)
        

