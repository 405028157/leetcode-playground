"""
不能用left == right，因为他们存的地址是不一样的，即使左右子树的值都相同
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def dfs(left: TreeNode, right: TreeNode):
             # left, right 都为 None
            if not (left or right):
                return True

            # left, right 其中之一为 None
            if not (left and right):
                return False
            
            if left.val != right.val:
                return False
            
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        if not root:
            return True
        return dfs(root.left, root.right)
            