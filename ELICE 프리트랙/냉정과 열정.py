def hot_cold(a):
    if len(a[a.index('냉정')+1:a.index('열정')]) > 0:
        return len(a[a.index('냉정')+1:a.index('열정')])
    else:
        return len(a[a.index('열정')+1:a.index('냉정')])
    
print(hot_cold(['냉정', '사랑', '사랑', '사랑', '열정', '사랑', '사랑']))  