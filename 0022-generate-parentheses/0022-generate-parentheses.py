class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = []
        def dfs(nopen, nclose):
            if nopen == nclose == n:
                res.append(''.join(tmp))
            if nopen < n:
                tmp.append('(')
                dfs(nopen+1, nclose)
                tmp.pop()
            if nclose < nopen:
                tmp.append(')')
                dfs(nopen, nclose+1)
                tmp.pop()
        dfs(0, 0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # tmp = []
        # def dfs(nopen, nclose):
        #     if nopen == nclose == n:
        #         res.append(''.join(tmp))
        #         return
        #     if nopen < n:
        #         tmp.append('(')
        #         dfs(nopen+1, nclose)
        #         tmp.pop()
        #     if nopen > nclose:
        #         tmp.append(')')
        #         dfs(nopen, nclose+1)
        #         tmp.pop()
        # dfs(0, 0)
        # return res

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