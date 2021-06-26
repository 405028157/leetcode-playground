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
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        pre = None
        def dfs(root: TreeNode):
            nonlocal pre
            if not root:
                return None
            
            dfs(root.right) # 这里可以不用接收返回值
            if pre != None:
                root.val = root.val + pre
            pre = root.val
            dfs(root.left) # 这里可以不用接收返回值
            return root
        
        return dfs(root)