class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(i):
            if i == len(nums):
                res.append(tmp.copy())
                return
            for n in nums:
                if n not in tmp:
                    tmp.append(n)
                    dfs(i+1)
                    tmp.pop()
        dfs(0)
        return res