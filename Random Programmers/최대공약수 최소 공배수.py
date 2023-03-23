def solution(n, m):
    

    
    # 최대 공약수
    answer = [] # 최대공약수
    if n > m:
        n, m = m, n

    max_div = 0
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            max_div = i

    answer.append(max_div)
    print(answer[0])
                
    # 최소 공배수

    # 큰수 % 작은수 == 0 => 
    # 큰수 / 작은수 == 몫 => 작은수 * 몫
     
    lcm = max_div*(n / max_div)*(m / max_div)    
        
    
    
    
    
    
    return answer