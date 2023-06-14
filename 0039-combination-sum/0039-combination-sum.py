class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(total, i):
            # if i >= len(candidates):
            #     return
            if total == target:
                res.append(tmp.copy())
                return
            elif total > target:
                return
            else:
                for j in range(i, len(candidates)):
                    tmp.append(candidates[j])
                    dfs(total + candidates[j], j)
                    tmp.pop()
        dfs(0, 0)
        return res