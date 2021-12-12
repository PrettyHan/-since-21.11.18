# 1193.분수찾기

X = int(input())
cycle = 0
while True:
	cycle += 1
	X -= cycle
	if X <= 0:
		X += cycle
		cycle += 1
		break
if cycle%2==0:
	print((cycle-X), '/', X, sep='')
else:
	print(X, '/', (cycle-X), sep='')