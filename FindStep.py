def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

from math import log    
def FindStep(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        phi = (1 + 5**0.5) / 2
        
        i = int(round(log(n * 5**0.5) / log(phi)))
        
        if F(i)<n:
            while F(i+1)<n:
                i+=1
            return min(abs(n-F(i)),abs(F(i+1)-n))
        else:
            while i>=1 and F(i-1)>n:
                i-=1
            return min(abs(n-F(i-1)),abs(F(i)-n))