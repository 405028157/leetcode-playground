# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return targetSum == 0

        # 到达叶子节点
        if not(root.left or root.right):
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)