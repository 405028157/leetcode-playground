# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        def dfs(inorder, postorder):
            if len(inorder) == 0:
                return None
            if len(inorder) == 1:
                return TreeNode(inorder[0])
            
            top = postorder.pop() # 不会再用到了，所以可以pop
            # 中序遍历的根节点index
            inorder_root = inorder.index(top)

            node = TreeNode(inorder[inorder_root])
            node.left = dfs(inorder[0:inorder_root], postorder[0:inorder_root])
            node.right = dfs(inorder[inorder_root + 1:], postorder[inorder_root:])
        
            return node
        
        return dfs(inorder, postorder)