class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minp, maxp = 1, 1
        for n in nums:
            tmp = maxp*n
            maxp = max(n, tmp, minp*n)
            minp = min(n, tmp, minp*n)
            res = max(res, maxp)
            if n == 0:
                maxp, minp = 1, 1
        return res