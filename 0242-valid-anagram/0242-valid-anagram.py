class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Both work, but Counter is nicer and slightly faster
        return Counter(s) == Counter(t)
        
        # d1, d2 = {}, {}
        # for c in s:
        #     d1[c] = d1.get(c, 0) + 1
        # for c in t:
        #     d2[c] = d2.get(c, 0) + 1
        # return d1 == d2
        
        