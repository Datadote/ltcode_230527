class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            L, R = i, i
            while L>=0 and R<len(s) and s[L]==s[R]:
                if (R-L+1) > len(res):
                    res = s[L:R+1]
                L -= 1
                R += 1
            L, R = i, i+1
            while L>=0 and R<len(s) and s[L]==s[R]:
                if (R-L+1) > len(res):
                    res = s[L:R+1]
                L -= 1
                R += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = ''
        # for i in range(len(s)):
        #     L, R = i, i
        #     while L>=0 and R<len(s) and s[L]==s[R]:
        #         if (R-L+1) > len(res):
        #             res = s[L:R+1]
        #         L -= 1
        #         R += 1
        #     L, R = i, i+1
        #     while L>=0 and R<len(s) and s[L]==s[R]:
        #         if (R-L+1) > len(res):
        #             res = s[L:R+1]
        #         L -= 1
        #         R += 1
        # return res
        
        # res = ''
        # max_len = 0
        # for i in range(len(s)):
        #     L, R = i, i
        #     while (L >= 0) and (R < len(s)) and (s[L]==s[R]):
        #         if R-L+1 > max_len:
        #             max_len = R - L + 1
        #             res = s[L:R+1]
        #         L -= 1
        #         R += 1
        #     L, R = i, i+1
        #     while (L >= 0) and (R < len(s)) and (s[L]==s[R]):
        #         if R-L+1 > max_len:
        #             max_len = R - L + 1
        #             res = s[L:R+1]
        #         L -= 1
        #         R += 1
        # return res