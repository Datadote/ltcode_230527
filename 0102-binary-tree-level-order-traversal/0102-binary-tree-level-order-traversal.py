# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dq = collections.deque([root])
        while len(dq) > 0:
            tmp = []
            for i in range(len(dq)):
                troot = dq.popleft()
                if troot:
                    tmp.append(troot.val)
                if troot and troot.left:
                    dq.append(troot.left)
                if troot and troot.right:
                    dq.append(troot.right)
            if tmp:
                res.append(tmp)
        return res