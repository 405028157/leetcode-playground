"""
优化思路，一是设计函数只传下标，而不是数组，二是对inorder建字典，方便找到根节点位置

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        """
        preorder[pre_left, ..., pre_right], inorder[in_left, ..., in_right]
        """
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])
        
            root_index = dic[preorder[pre_left]]
            node = TreeNode(preorder[pre_left])
            # [in_left, root_index - 1]  左子树节点数量 root_index - in_left
            node.left = build(pre_left + 1, pre_left + root_index - in_left, in_left, root_index - 1)
            node.right = build(pre_left + root_index - in_left + 1, pre_right, root_index + 1, in_right)
            return node

        dic = {element: i for i, element in enumerate(inorder)}
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)