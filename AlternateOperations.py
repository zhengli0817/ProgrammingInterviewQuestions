def AlternateOperations(n):
    if (not isinstance(n, int)) or (n<=1): return 0 
    res=1
    if (n==1): return res
    for i in range(2,n+1):
        if (i%3==2):
            res += i
        elif (i%3==0):
            res *= i
        else:
            res -= i
    return res
        
             