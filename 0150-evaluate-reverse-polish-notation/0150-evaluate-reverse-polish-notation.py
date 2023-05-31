class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dmap = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)
        }
        
        for token in tokens:
            if token in dmap:
                b, a = stack.pop(), stack.pop()
                stack.append(dmap[token](a,b))
            else:
                stack.append(int(token))
        return stack[0]