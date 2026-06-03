class Solution:
    def partition(self, head, x: int):
        before=bt=ListNode(0); after=at=ListNode(0)
        while head:
            if head.val < x: bt.next=head; bt=bt.next
            else: at.next=head; at=at.next
            head=head.next
        at.next=None; bt.next=after.next
        return before.next
