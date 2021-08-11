"""
有bug，问题在于ans是个局部变量，只能存根节点这个pathSum的ans数量
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        ans = 0
        
        def dfs(node: TreeNode, curSum):
            nonlocal ans
            if not node:
                return 0
            
            if node.val == curSum:
                ans += 1
            
            dfs(node.left, curSum - node.val)
            dfs(node.right, curSum - node.val)
        
        dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return ans
        
            