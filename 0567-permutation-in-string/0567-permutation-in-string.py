class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count1, count2 = [0]*26, [0]*26
        matches = 0
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            count1[idx] += 1
            idx = ord(s2[i]) - ord('a')
            count2[idx] += 1
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[R]) - ord('a')
            count2[idx] += 1
            if count1[idx] == count2[idx]:
                matches += 1
            elif count1[idx]+1 == count2[idx]:
                matches -= 1
            
            idx = ord(s2[L]) - ord('a')
            count2[idx] -= 1
            if count1[idx] == count2[idx]:
                matches += 1
            elif count1[idx]-1 == count2[idx]:
                matches -= 1
            L += 1
        return matches == 26
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count1 = Counter(s1)
        # for i in range(len(s2)):
        #     if count1 == Counter(s2[i:i+len(s1)]):
        #         return True
        # return False