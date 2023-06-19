class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        for i in range(len(cost)-1, -1, -1):
            min_c = cost[i] + min(dp)
            dp[0], dp[1] = dp[1], min_c
        return min(dp)