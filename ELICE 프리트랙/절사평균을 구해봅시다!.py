def myMean(a):
    ans = 0
    a.remove(min(a))
    a.remove(max(a))
    for i in a:
        ans += i
    ans2 = ans/len(a)
    return ans2    
print(myMean([1, 2, 3, 4, 5, 6, 7]))
