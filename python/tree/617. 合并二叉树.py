# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 俩者都为None
        if not (root1 or root2):
            return None
        
        # 如果其中一个为None，让root2为None
        if not (root1 and root2):
            if not root1:
                root1, root2 = root2, root1
        
            node = TreeNode(root1.val)
            node.left = self.mergeTrees(root1.left, None)
            node.right = self.mergeTrees(root1.right, None)
            return node
        
        # 俩者都不为None
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node

"""
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        # 俩者都不为None
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node
"""