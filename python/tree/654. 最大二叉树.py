# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        # 区间是 [left_index, right_index]
        def build(left_index, right_index):
            if left_index > right_index:
                return None
            if left_index == right_index:
                return TreeNode(nums[left_index])
            
            root_value = max(nums[left_index: right_index + 1])
            root_index = dic[root_value]
            node = TreeNode(nums[root_index])
            node.left = build(left_index, root_index - 1)
            node.right = build(root_index + 1, right_index)
            return node

        dic = {element: i for i, element in enumerate(nums)}
        return build(0, len(nums) - 1)
