N = int(input())
i = 1
i_ans = 0
i_list = []
while True:
    if N <= i:
        break
    elif N % i == 0:
       i_ans += i
       i_list.append(i)
    i += 1
if N == i_ans:
    ans = f"{N}"+" "+"="+" "+str(i_list[0])+" "
    for a in range(1, len(i_list)):
        ans += "+"+" "+str(i_list[a])+" "
    print(ans)
else:
    print(f"{N} is NOT perfect.")    

