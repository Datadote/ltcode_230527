class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp_num = 'abcdefghijklmnopqrstuvwrxyz0123456789'
        L, R = 0, len(s)-1
        while L < R:
            while L<R and s[L].lower() not in alp_num:
                L += 1
            while L<R and s[R].lower() not in alp_num:
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # alp_num = set('abcdefghijklmnopqrstuvwxyz0123456789')
        # L, R = 0, len(s)-1
        # while L <= R:
        #     if s[L].lower() not in alp_num:
        #         L += 1
        #         continue
        #     if s[R].lower() not in alp_num:
        #         R -= 1
        #         continue
        #     if s[L].lower() != s[R].lower():
        #         return False
        #     L += 1
        #     R -= 1
        # return True
        
        # alph_num = 'abcdefghijklmnopqrstuvwrxyz0123456789'
        # L, R = 0, len(s)-1
        # while L < R:
        #     while L < R and s[L].lower() not in alph_num:
        #         L += 1
        #     while L < R and s[R].lower() not in alph_num:
        #         R -= 1
        #     if s[L].lower() != s[R].lower():
        #         return False
        #     L += 1
        #     R -= 1
        # return True
        
        # alph_num = 'abcdefghijklmnopqrstuvwrxyz0123456789'
        # tmp = ''
        # s = s.lower()
        # for c in s:
        #     if c in alph_num:
        #         tmp += c
        # L, R = 0, len(tmp)-1
        # while L < R:
        #     if tmp[L] != tmp[R]:
        #         return False
        #     L += 1
        #     R -= 1
        # return True