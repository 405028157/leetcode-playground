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
        # print(self.sum)
        if not root:
            return False
        
        self.sum += root.val
        # 到达叶子节点
        if not(root.left or root.right):
            temp = self.sum
            self.sum -= root.val
            return temp == targetSum
        
        l = self.hasPathSum(root.left, targetSum)
        r = self.hasPathSum(root.right, targetSum)
        self.sum -= root.val
        return l or r