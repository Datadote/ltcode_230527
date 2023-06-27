class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0, dp1 = 0, 0
        for i in range(len(cost)):
            dp0, dp1 = dp1, min(dp0, dp1) + cost[i]
        return min(dp0, dp1)

        # dp0, dp1 = cost[0], cost[1]
        # for i in range(2, len(cost)):
        #     dp0, dp1 = dp1, min(dp0, dp1) + cost[i]
        # return min(dp0, dp1)
        
        # dp0, dp1 = cost[0], cost[1]
        # for i in range(2, len(cost)):
        #     dp0, dp1 = dp1, min(dp0, dp1) + cost[i]
        # return min(dp0, dp1)
    
    # dp = [0, 0]
        # for i in range(len(cost)-1, -1, -1):
        #     min_c = cost[i] + min(dp)
        #     dp[0], dp[1] = dp[1], min_c
        # return min(dp)