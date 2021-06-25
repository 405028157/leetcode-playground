"""
用后序遍历，从下往上找要删除的节点，此时找到每个要删除的节点不可能同时有左右子树，因为要么左子树更小，早就被删，要么右子树更大，也早就被删。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        
        # 叶子节点
        if not (root.left or root.right):
            if root.val > high or root.val < low:
                return None
            return root
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val > high or root.val < low:
            if not (root.left or root.right):
                root = None
            elif not root.left:
                root = root.right
            else:
                root = root.left
        
        return root