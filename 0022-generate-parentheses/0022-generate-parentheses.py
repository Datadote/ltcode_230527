class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(nopen, nclose):
            if nopen == nclose == n:
                res.append(''.join(stack))
                return
            if nopen < n:
                stack.append('(')
                backtrack(nopen+1, nclose)
                stack.pop()
            if nopen > nclose:
                stack.append(')')
                backtrack(nopen, nclose+1)
                stack.pop()
        backtrack(0, 0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # stack = []
        # def backtrack(nopen, nclose):
        #     if nopen == nclose == n:
        #         res.append(''.join(stack))
        #         return
        #     if nopen < n:
        #         stack.append('(')
        #         backtrack(nopen+1, nclose)
        #         stack.pop()
        #     if nopen > nclose:
        #         stack.append(')')
        #         backtrack(nopen, nclose+1)
        #         stack.pop()
        # backtrack(0, 0)
        # return res