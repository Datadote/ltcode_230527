# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dq = collections.deque()
        if root:
            dq.append(root)
        while dq:
            tmp = []
            for i in range(len(dq)):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(tmp)
        return res
        
        # res = []
        # dq = collections.deque([root])
        # while len(dq) > 0:
        #     tmp = []
        #     for i in range(len(dq)):
        #         troot = dq.popleft()
        #         if troot:
        #             tmp.append(troot.val)
        #         if troot and troot.left:
        #             dq.append(troot.left)
        #         if troot and troot.right:
        #             dq.append(troot.right)
        #     if tmp:
        #         res.append(tmp)
        # return res