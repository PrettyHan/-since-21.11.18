answers = [1,2,3,4,5]

p2 = []
aws = []
count1 = 0
for i in range(1,6):
    p2.append(2)
    p2.append(i)

print(len(p2))

while len(p2) <= 10000:
    p2 += p2

for i in answers:
    if i in p2:
        count1 += 1
print(count1)