# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

        # cur = root
        # while cur:
        #     if cur.val < p.val and cur.val < q.val:
        #         cur = cur.right
        #     elif cur.val > p.val and cur.val > q.val:
        #         cur = cur.left
        #     else:
        #         return cur