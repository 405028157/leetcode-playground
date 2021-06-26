"""
直观解法......
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        val_list = []

        def dfs(root: TreeNode):
            if not root:
                return
            
            dfs(root.left)
            val_list.append(root.val)
            dfs(root.right)

        dfs(root)
        dic = {element: i for i, element in enumerate(val_list)}

        def convert(root: TreeNode):
            if not root:
                return None
            
            root.val = sum(val_list[dic[root.val]:])
            convert(root.left)
            convert(root.right)
        
        convert(root)
        return root