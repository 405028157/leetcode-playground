# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        def build(left_index, right_index):
            if left_index > right_index:
                return None
            root_value = max(nums[left_index: right_index+1])
            root_index = hash_nums[root_value]
            root = TreeNode(root_value)
            root.left = build(left_index, root_index-1)
            root.right = build(root_index+1, right_index)
            return root


        hash_nums = {nums[i]:i for i in range(len(nums))}
        return build(0, len(nums)-1)