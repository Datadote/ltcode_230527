class Solution:
    def isValid(self, s: str) -> bool:
        dcheck = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in dcheck and stack:
                if stack.pop() != dcheck[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        # dR2L = {')':'(', ']':'[', '}':'{'}
        # for c in s:
        #     if c not in dR2L:
        #         stack.append(c)
        #     elif stack and dR2L[c]==stack.pop():
        #         continue
        #     else:
        #         return False
        # return len(stack) == 0