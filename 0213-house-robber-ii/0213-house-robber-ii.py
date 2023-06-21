class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            rob1, rob2 = 0,0
            for n in nums:
                rob1, rob2 = rob2, max(rob1+n, rob2)
            return rob2
        return max(rob1(nums[:-1]), rob1(nums[1:]), nums[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def rob1(nums):
        #     dp0, dp1 = 0, 0
        #     for i in range(len(nums)):
        #         dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        #     return dp1
        # return max(rob1(nums[1:]), rob1(nums[:-1]), nums[0])