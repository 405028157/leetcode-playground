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

        # 作用是判断以该节点为根的二叉树，是否是镜像对称的
        def dfs(node: TreeNode):
            print(node)
            if not node:
                return True

            left = node.left
            right = node.right
            print(f'left = {left}, right = {right}')

            # left, right 都为 None
            if not (left or right):
                return True

            # left, right 其中之一为 None
            if not (left and right):
                return False

            return left.val == right.val and dfs(left) and dfs(right)
        
        return dfs(root)
            