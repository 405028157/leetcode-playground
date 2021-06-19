# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0
    
    def height(self, root: TreeNode):
        if not root:
            return 0
        
        hl = self.height(root.left)
        hr = self.height(root.right)

        if hl == -1 or hr == -1 or abs(hl - hr) > 1:
            return -1
        
        return max(hl, hr) + 1