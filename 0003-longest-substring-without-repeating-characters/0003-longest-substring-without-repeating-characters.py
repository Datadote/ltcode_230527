class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        L = 0
        for i,c in enumerate(s):
            if c not in char_set:
                char_set.add(c)
                max_len = max(max_len, len(char_set))
            else:
                while c in char_set:
                    char_set.remove(s[L])
                    L += 1
                char_set.add(c)
        return max_len
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # charSet = set()
        # max_len = 0
        # L = 0
        # for c in s:
        #     while c in charSet:
        #         charSet.remove(s[L])
        #         L += 1
        #     charSet.add(c)
        #     max_len = max(max_len, len(charSet))
        # return max_len
        
        # char_set = set()
        # max_len = 0
        # L = 0
        # for R in range(len(s)):
        #     while s[R] in char_set:
        #         char_set.remove(s[L])
        #         L += 1
        #     char_set.add(s[R])
        #     max_len = max(max_len, len(char_set))
        # return max_len