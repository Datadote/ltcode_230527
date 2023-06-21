class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 0, 1
        for i in range(n):
            dp0, dp1 = dp1, dp0+dp1
        return dp1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if n ==1 or n==2:
        #     return n
        # dp0, dp1 = 1, 2
        # for i in range(n-2):
        #     dp0, dp1 = dp1, dp0+dp1
        # return dp1

        # # T: O(n), S: O(1)
        # def fibo2(n):
        #     if n==1 or n==2:
        #         return n
        #     n1, n2 = 1, 2
        #     for i in range(n-2):
        #         n1, n2 = n2, n1+n2
        #     return n2
        # return fibo2(n)
            
        # # T: O(n), S: O(n)
        # d = {1:1, 2:2}
        # def fibo(n):
        #     if n in d:
        #         return d[n]
        #     tmp = fibo(n-1) + fibo(n-2)
        #     d[n] = tmp
        #     return tmp
        # return fibo(n)