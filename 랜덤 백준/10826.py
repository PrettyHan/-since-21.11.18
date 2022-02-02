# 10826 피보나치 수 4

n = int(input()) # n = 5

big_list = [0 for i in range(10001)] # 00000000000000000000000000000000

big_list[1] = 1 # 더하기 위해 지정


             #(2, 6)  
for j in range(2, n+1): # j = 2, 3 ,4, 5
    big_list[j] = big_list[j-1] + big_list[j-2]        #[0,1,0,0,0,0,0,0 ~]
            #1             # 1             # 0          [0,1,1]
            #2             # 1             # 1          [0,1,1 + 2]
            #3             # 2             # 1          [0,1,1,2 + 3]
            #5             # 3             # 2          [0,1,1,2,3 + 5]
                
print(big_list[n])# n = 5, result = 5
