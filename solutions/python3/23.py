# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    def mergeKLists(self, lists):
        q = []
        for i in range(len(lists)):
            while lists[i]:
                q += lists[i],
                lists[i] = lists[i].next
        root = cur = ListNode(0)
        for h in sorted(q, key = lambda x: x.val):
            cur.next = cur = h
        return root.next
    '''

    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None
        size = len(lists)
        return self.merge_sort(lists, 0, size - 1)

    def merge_sort(self, lists, left: int, right: int) -> ListNode:
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        node_left = self.merge_sort(lists, left, mid)
        node_right = self.merge_sort(lists, mid + 1, right)
        return self.merge(node_left, node_right)

    def merge(self, a , b ) -> ListNode:
        root = ListNode(-1)
        cur = root
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        if a:
            cur.next = a
        if b:
            cur.next = b
        return root.next

a = Solution()


