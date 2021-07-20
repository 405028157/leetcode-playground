# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_depth = float('inf')

        def dfs(node: TreeNode, depth: int):
            nonlocal min_depth
            if not(node.left or node.right):
                min_depth = min(depth, min_depth)
            
            if node.left:
                dfs(node.left, depth + 1)
            
            if node.right:
                dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return min_depth