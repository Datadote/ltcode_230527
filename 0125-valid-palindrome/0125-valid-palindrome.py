class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = 'abcdefghijklmnopqrstuvwxyz0123456789'
        tmp = ''
        s = s.lower()
        # s = [c for c in s]
        s = list(s)
        for c in s:
            if c in alpha_num:
                tmp += c
        L, R = 0, len(tmp)-1
        while L < R:
            if tmp[L] != tmp[R]:
                return False
            L += 1
            R -= 1
        return True