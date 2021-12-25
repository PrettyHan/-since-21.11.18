
hello = input()
ans = 10
for i in range(1, len(hello)):
    if hello[i-1] == hello[i]:
        ans += 5  
    else:
        ans += 10

print(ans)    