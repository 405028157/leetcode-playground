# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key > root.val:
            self.deleteNode(root.right, key)
        elif key < root.val:
            self.deleteNode(root.left, key)
        else:
            print(root)
            if root.left and root.right:
                min_rnode = self.find_min(root.right)
                root.val = min_rnode.val
                self.deleteNode(root.right, root.val)
            else:
                # 严格的条件要先判断，
                # 左右子树都为空，其实可以省略，下面俩个分支能帮忙做
                if not (root.left or root.right):
                    """
                    这里有bug，使root指向None，并不会释放root原来指向的内存空间的对象
                    """
                    root = None
                # 左子树为空
                elif not root.left:
                    root = root.right
                # 右子树为空
                elif not root.right:
                    root = root.left
        return root

    def find_min(self, root: TreeNode):
        if not root:
            return None
        
        if not root.left:
            return root

        return self.find_min(root.left)