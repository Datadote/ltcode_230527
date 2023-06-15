class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)
        }
        
        for t in tokens:
            if t not in d:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(d[t](a,b))
        return stack[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dmap = {'+': lambda a,b: a+b,
        #         '-': lambda a,b: a-b,
        #         '*': lambda a,b: a*b,
        #         '/': lambda a,b: int(a/b)
        #        }
        # stack = []
        # for c in tokens:
        #     if c not in dmap:
        #         stack.append(int(c))
        #     else:
        #         b, a = stack.pop(), stack.pop()
        #         stack.append(dmap[c](a,b))
        # return stack[0]
        
#         stack = []
#         dmap = {
#             '+': lambda a,b: a+b,
#             '-': lambda a,b: a-b,
#             '*': lambda a,b: a*b,
#             '/': lambda a,b: int(a/b)
#         }
        
#         for token in tokens:
#             if token in dmap:
#                 b, a = stack.pop(), stack.pop()
#                 stack.append(dmap[token](a,b))
#             else:
#                 stack.append(int(token))
#         return stack[0]