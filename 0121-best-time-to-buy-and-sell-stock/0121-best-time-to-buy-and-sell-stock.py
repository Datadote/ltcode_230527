class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p = math.inf, 0
        for p in prices:
            min_p = min(min_p, p)
            max_p = max(max_p, p-min_p)
        return max_p
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_p, min_price = 0, prices[0]
        # for p in prices:
        #     min_price = min(min_price, p)
        #     max_p = max(max_p, p-min_price)
        # return max_p