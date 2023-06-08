# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, h):
            if not root:
                return [True, 0]
            left = dfs(root.left, h)
            right = dfs(root.right, h)
            balanced = (abs(left[1] - right[1]) < 2
                        and left[0]
                        and right[0]
                       )
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root, 0)[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def dfs(root, h):
        #     if not root:
        #         return [True, 0]
        #     left = dfs(root.left, h)
        #     right = dfs(root.right, h)
        #     balanced = (left[0]
        #                 and right[0]
        #                 and abs(left[1] - right[1]) < 2
        #                )
        #     return [balanced, 1 + max(left[1], right[1])]
        # return dfs(root, 0)[0]