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
            balanced = (left[0]
                        and right[0]
                        and abs(left[1] - right[1]) < 2
                       )
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root, 0)[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def max_depth(root):
        #     if not root:
        #         return 0
        #     left = max_depth(root.left)
        #     right = max_depth(root.right)
        #     if abs(left-right) > 1:
        #         return False
        #     return 1 + max(left, right)
        # if not root or max_depth(root):
        #     return True
        # else:
        #     return False