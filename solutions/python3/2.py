# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0
        dummy = cur = ListNode(-1)
        while l1 or l2 or left:
            left, sm = divmod(sum(l and l.val or 0 for l in (l1, l2)) + left, 10)
            cur.next = ListNode(sm)
            cur = cur.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return dummy.next

a = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s1 = sum(l.val for l in (l1, l2))
print(s1)
l1 = l1.next
l2 = l2.next

s2 = sum(l and l.val or 0 for l in (l1, l2))
print(s2)

l3 = a.addTwoNumbers(l1, l2)
print("end")
