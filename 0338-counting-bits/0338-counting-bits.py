class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        os = 1
        for i in range(1, n+1):
            if os*2 == i:
                os = i
            dp[i] = 1 + dp[i-os]
        return dp
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def numBits(n):
        #     res = 0
        #     while n:
        #         res += n % 2
        #         n = n >> 1
        #     return res
        # res = []
        # for i in range(n+1):
        #     res.append(numBits(i))
        # return res