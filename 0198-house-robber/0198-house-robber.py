class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0, dp1 = 0, nums[0]
        for i in range(1, len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # rob1, rob2 = 0, 0
        # for n in nums:
        #     rob1, rob2 = rob2, max(rob1+n, rob2)
        # return max(rob1, rob2)