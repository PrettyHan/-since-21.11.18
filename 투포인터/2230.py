import sys

N, M = map(int, sys.stdin.readline().split())

arr = sorted(list(int(sys.stdin.readline().rstrip()) for i in range(N)))
diff = []
start = 0
end = 0
while start < N and end < N:
    check = arr[end] - arr[start]
    if check == M:
        diff.append(check)
        break
    if check < M:
        end += 1
        continue
    diff.append(check)
    start += 1

diff.sort()

print(diff[0])