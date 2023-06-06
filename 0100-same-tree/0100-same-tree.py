# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        resp, resq = [], []
        def dfs(root, t):
            if not root:
                t.append([])
                return
            t.append(root.val)
            dfs(root.left, t)
            dfs(root.right, t)
        dfs(p, resp)
        dfs(q, resq)
        return resp == resq