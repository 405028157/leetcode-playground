# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        cur = root
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            top = stack.pop()
            res.append(top.val)
            cur = top.right # 每个节点都是根节点，既然访问过根节点，就应该访问右子节点了
        
        return res