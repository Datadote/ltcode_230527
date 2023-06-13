# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]): 
        def dfs(p, q):
            if not p and not q:
                return True
            if (not p
                or not q
                or p.val != q.val
               ):
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p, q)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if p is None and q is None:
        #     return True
        # if (p is None
        #     or q is None
        #     or p.val != q.val
        #    ):
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # if not p and not q:
        #     return True
        # if (not p
        #     or not q
        #     or p.val != q.val
        #    ):
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # if not p and not q:
        #     return True
        # if (not p
        #     or not q
        #     or p.val != q.val
        #    ):
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # resp, resq = [], []
        # def dfs(root, t):
        #     if not root:
        #         t.append(None)
        #         return
        #     t.append(root.val)
        #     dfs(root.left, t)
        #     dfs(root.right, t)
        # dfs(p, resp)
        # dfs(q, resq)
        # return resp == resq