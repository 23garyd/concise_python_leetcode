# coding=gbk
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#点简化
class Solution:
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        first = head.next
        second = head
        second.next = self.swapPairs(first.next)
        first.next = second
        return first
    '''

    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        curr = new_head
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            curr.next = node2
            node1.next = node2.next
            node2.next = node1
            curr = node1
        return new_head.next


a = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
res = a.swapPairs(l1)
print(res)