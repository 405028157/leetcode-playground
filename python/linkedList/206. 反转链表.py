# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        ret = self.reverseList(head.next)
        # 这里下一层的递归head是本层的head.next，两层递归都修改到了同一个节点的next指针，但是由于最外层的递归最后执行，所以内层递归的head.next = null操作先执行，然后被外层的head.next.next = head覆盖，不会让链表断开
        head.next.next = head
        head.next = None
        
        return ret