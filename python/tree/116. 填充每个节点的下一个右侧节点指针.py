import collections

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q = collections.deque()
        q.append(root)

        while q:
            last_node = None
            for _ in range(len(q)):
                cur_node = q.popleft()
                if last_node:
                    last_node.next = cur_node
                last_node = cur_node

                cur_node.left and q.append(cur_node.left)
                cur_node.right and q.append(cur_node.right)
            cur_node.next = None
            
        return root