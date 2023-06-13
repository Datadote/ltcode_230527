# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        return dfs(root)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1 + max(dfs(root.left), dfs(root.right))
        # return dfs(root)

        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1 + max(dfs(root.left), dfs(root.right))
        # return dfs(root)

        # res = 0
        # def dfs(root, h):
        #     nonlocal res
        #     if not root:
        #         res = max(res, h)
        #         return
        #     dfs(root.left, h+1)
        #     dfs(root.right, h+1)
        # dfs(root, 0)
        # return res