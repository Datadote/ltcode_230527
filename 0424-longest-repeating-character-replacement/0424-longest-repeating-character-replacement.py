class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        L = 0
        for R in range(len(s)):
            count[s[R]] += 1
            while (R-L+1 - max(count.values())) > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res