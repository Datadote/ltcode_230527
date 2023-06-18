class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        for i in range(len(s2)):
            if count1 == Counter(s2[i:i+len(s1)]):
                return True
        return False