class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            dp0, dp1 = 0, 0
            for i in range(len(nums)):
                dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
            return dp1
        return max(rob1(nums[1:]), rob1(nums[:-1]), nums[0])