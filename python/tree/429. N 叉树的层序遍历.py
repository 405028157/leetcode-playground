import collections

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root:
            return []
        q = collections.deque()
        res = []
        
        q.append(root)

        while q:
            cur_layer = []
            for _ in range(len(q)):
                cur = q.popleft()
                cur_layer.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        q.append(child)

            res.append(cur_layer)
        
        return res