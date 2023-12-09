class Solution:
    def swapPairs(self, head: optional[listNode]) -> optional[listNode]:

        if not head or not head.next: return head

        dummy = listNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next
        
        return dummy.next