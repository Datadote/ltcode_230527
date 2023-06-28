class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rem = set(range(len(nums)+1))
        for n in nums:
            rem.remove(n)
        return rem.pop()