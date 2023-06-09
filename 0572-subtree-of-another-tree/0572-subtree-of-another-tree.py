# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if (not p
                or not q
                or p.val != q.val
               ):
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        def dfs(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False
            if isSame(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def isSame(p, q):
#             if not p and not q:
#                 return True
#             if (not p
#                 or not q
#                 or p.val != q.val
#                ):
#                 return False
#             return isSame(p.left, q.left) and isSame(p.right, q.right)
    
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         if isSame(root, subRoot):
#             return True
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#         def isSame(p, q):
#             if not p and not q:
#                 return True
#             if (not p
#                 or not q
#                 or p.val != q.val
#                ):
#                 return False
#             return isSame(p.left, q.left) and isSame(p.right, q.right)
        
#         # edges cases. If subtRoot is null, then it is Subtree
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         if isSame(root, subRoot):
#             return True
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)