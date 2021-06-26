"""
直观解法......
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归
    def convertBST2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        total = 0
        def dfs(root: TreeNode):
            nonlocal total
            if not root:
                return None
            
            dfs(root.right) # 这里可以不用接收返回值
            total += root.val
            root.val = total
            dfs(root.left) # 这里可以不用接收返回值
            return root
        
        return dfs(root)
    
    # 迭代
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        stack = []
        cur = root
        total = 0

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            
            top = stack.pop()
            total += top.val
            top.val = total
            cur = top.left
        
        return root