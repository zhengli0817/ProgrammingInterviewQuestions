#https://leetcode.com/problems/climbing-stairs/
#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# This is the same problem as finding the nth Fibonnaci number

# ref: http://www.tangjikai.com/algorithms/leetcode-70-climbing-stairs

def ClimbStairs(n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]

# This second solution is not as clear not the first solution, but saves some space              
def ClimbStairs2(n):
        p = q = 1
        
        for i in range(1, n):
            tmp = q
            q += p
            p = tmp
        
        return q