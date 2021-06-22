# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        top = preorder.pop(0)
        # 中序遍历的根节点index，左子树的节点数量也正好是inorder_root
        inorder_root = inorder.index(top)

        node = TreeNode(top)
        node.left = self.buildTree(preorder[0:inorder_root], inorder[0:inorder_root])
        node.right = self.buildTree(preorder[inorder_root:], inorder[inorder_root + 1:])
        
        return node