# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        max_num = max(nums)
        root_index = nums.index(max_num)

        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[0:root_index])
        node.right = self.constructMaximumBinaryTree(nums[root_index + 1:])

        return node