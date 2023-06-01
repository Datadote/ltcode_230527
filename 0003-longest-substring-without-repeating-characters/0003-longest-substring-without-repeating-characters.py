class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        L = 0
        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])
            max_len = max(max_len, R-L+1)
            # max_len = max(max_len, len(char_set))
        return max_len