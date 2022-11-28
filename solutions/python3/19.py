class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]
        while head:
            arr.append(head)
            head = head.next
        for _ in range(n + 1):
            pre = arr.pop()
        pre.next = pre.next.next
        return dummy.next

    '''
    
       def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        while n:
            curr = curr.next
            n -= 1
        while curr:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next
        return dummy.next
    
    '''