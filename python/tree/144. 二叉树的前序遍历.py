# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        cur = root
        stack = []

        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            
            top = stack.pop()
            cur = top.right
        
        return res