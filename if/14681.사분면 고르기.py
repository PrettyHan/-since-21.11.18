# 14681번. 사분면 고르기

x = input()
y = input()
x = int(x)
y = int(y)

x != 0
y != 0

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:    
    print("2")
elif x < 0 and y < 0:
    print("3") 
elif x > 0 and y < 0:
    print("4")
      