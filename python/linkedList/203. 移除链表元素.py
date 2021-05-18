"""
1. 注意链表的定义方式
2. 哨兵节点sentinel, 广泛应用于树和链表中，如伪头、伪尾、标记等，它们是纯功能的，通常不保存任何数据，其主要目的是使链表标准化，如使链表永不为空、永不无头、简化插入和删除。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                # print(f'curr={curr}, curr.next={curr.next}')
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

s = Solution()
s.removeElements(l1, 2)
# 在这里打断点调试，可以看链表结构
print(s)