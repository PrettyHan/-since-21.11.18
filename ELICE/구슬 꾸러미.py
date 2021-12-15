red = 250
blue = 40
white = 10

weight = int(input())

var1 = weight // red

var2 = weight % red

var3 = var2 // blue 

var4 = var2 % blue

var5 = var4 // white

if weight < white:
    print(-1)
elif weight % white != 0:
    print(-1)    
else:
    print(var1+var3+var5)