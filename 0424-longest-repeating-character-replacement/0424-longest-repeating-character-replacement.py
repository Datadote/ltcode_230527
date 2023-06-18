class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        res = 0
        L, R = 0, 0
        while R < len(s):
            d[s[R]] += 1
            R += 1
            while (R-L)-max(d.values()) > k:
                d[s[L]] -= 1
                L += 1
            res = max(res, R-L)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_len = 0
        # d = defaultdict(int)
        # L = 0
        # for R in range(len(s)):
        #     d[s[R]] += 1
        #     while (R-L+1) - max(d.values()) > k:
        #         d[s[L]] -= 1
        #         L += 1
        #     max_len = max(max_len, R-L+1)
        # return max_len
        
#         d = defaultdict(int)
#         L = 0
#         max_len = 0
#         for R in range(len(s)):
#             d[s[R]] += 1
#             while (R-L+1) - max(d.values()) > k:
#                 d[s[L]] -= 1
#                 L += 1
#             max_len = max(max_len, R-L+1)
#         return max_len
    
        # count = defaultdict(int)
        # res = 0
        # L = 0
        # for R in range(len(s)):
        #     count[s[R]] += 1
        #     while (R-L+1 - max(count.values())) > k:
        #         count[s[L]] -= 1
        #         L += 1
        #     res = max(res, R-L+1)
        # return res