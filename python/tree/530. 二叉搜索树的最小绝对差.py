# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_abs = float('inf')
        self.pre = None

        def inorder(node: TreeNode):
            if not node:
                return
            
            inorder(node.left)

            if not self.pre:
                self.pre = node.val
            else:
                self.min_abs = min(abs(node.val - self.pre), self.min_abs)
            
            inorder(node.right)
        
        inorder(root)
        return self.min_abs

