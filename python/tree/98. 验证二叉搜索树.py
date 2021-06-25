# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
二叉树的中序遍历是递增的
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')

        def is_valid(node: TreeNode):
            nonlocal pre
            if not node:
                return True
            
            if not is_valid(node.left):
                return False
            
            if node.val <= pre:
                return False
            
            pre = node.val

            return is_valid(node.right)
        
        return is_valid(root)
