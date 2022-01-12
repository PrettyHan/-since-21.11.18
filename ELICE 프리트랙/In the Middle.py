a = []
count = 0
while True:
    N = int(input())
    a.append(N)
    count += 1
    if count == 3:
        break
a.sort()
print(a[1])
