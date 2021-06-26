# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])

        # mid = int((len(nums) - 1) / 2)，也可以，但是树的结构会不一样
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root