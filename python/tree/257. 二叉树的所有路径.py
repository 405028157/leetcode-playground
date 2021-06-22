# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if not root:
            return []
        res = []

        def dfs(node: TreeNode, path: list):
            nonlocal res

            # 到达叶子节点
            if not(node.left or node.right):
                res.append('->'.join(map(str, path)))
            
            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])

        dfs(root, [root.val])
        return res