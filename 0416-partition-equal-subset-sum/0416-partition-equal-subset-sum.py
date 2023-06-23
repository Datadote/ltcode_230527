class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total / 2
        sums = set()
        sums.add(0)
        for n in nums:
            tmp = set()
            for s in sums:
                tmp.add(s + n)
                tmp.add(s)
            sums = tmp
        return target in sums