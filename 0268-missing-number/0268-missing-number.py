class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
        
        
        # rem = set(range(len(nums)+1))
        # for n in nums:
        #     rem.remove(n)
        # return rem.pop()