class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        min_k = R
        def num_hrs(piles, k):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k)
            return hrs
        while L <= R:
            M = L + (R-L)//2
            hrs = num_hrs(piles, M)
            if hrs > h:
                L = M + 1
            else:
                min_k = min(min_k, M)
                R = M -1
        return min_k
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def num_hrs(piles, k):
        #     hrs = 0
        #     for p in piles:
        #         hrs += math.ceil(p/k)
        #     return hrs
        # L, R = 1, max(piles)
        # mink = R
        # while L <= R:
        #     M = L + (R-L)//2
        #     hrs = num_hrs(piles, M)
        #     if hrs > h:
        #         L = M + 1
        #     else:
        #         mink = min(mink, M)
        #         R = M - 1
        # return mink
        
#         def num_hrs(piles, k):
#             hrs = 0
#             for p in piles:
#                 hrs += math.ceil(p/k)
#             return hrs
        
#         L, R = 1, max(piles)
#         min_k = R
#         while L <= R:
#             M = L + (R-L)//2
#             hrs = num_hrs(piles, M)
#             if hrs <= h:
#                 min_k = min(min_k, M)
#                 R = M - 1
#             else:
#                 L = M + 1
#         return min_k