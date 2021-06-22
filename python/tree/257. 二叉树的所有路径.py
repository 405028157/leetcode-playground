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
            
            # 这里一定不能append，否则到处都只是一个path
            path = path + [node.val]
            # 到达叶子节点
            if not(node.left or node.right):
                res.append('->'.join(map(str, path)))
            
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, [])
        return res

"""
最快版本，注意push，pop时机
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root):
            if not root:
                return 

            path.append(str(root.val))
            if not root.right and not root.left:
                res.append('->'.join(path))

            dfs(root.left)
            dfs(root.right)

            path.pop()


        path = []
        res = []

        dfs(root)

        return res
"""