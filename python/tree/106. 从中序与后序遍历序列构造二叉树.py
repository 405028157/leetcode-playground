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
            
            # 中序遍历的根节点index
            inorder_root = 0
            print(postorder)
            while inorder_root < len(inorder) and inorder[inorder_root] != postorder[-1]:
                inorder_root += 1
                # print(f'inorder_root = {inorder_root}, len(inorder) = {len(inorder)}, inorder = {inorder}, inorder[inorder_root] = {inorder[inorder_root]}, postorder = {postorder}, postorder[-1] = {postorder[-1]}')
            
            # 后序遍历的右子树第一个节点index
            postorder_right = 0
            while inorder_root + 1 < len(inorder) and postorder[postorder_right] != inorder[inorder_root + 1]:
                postorder_right += 1
            
            node = TreeNode(inorder[inorder_root])
            node.left = dfs(inorder[0:inorder_root], postorder[0:postorder_right])
            node.right = dfs(inorder[inorder_root + 1:], postorder[postorder_right:-1])
        
            return node
        
        return dfs(inorder, postorder)