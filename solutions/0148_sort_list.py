class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        slow,fast=head,head.next
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        mid=slow.next; slow.next=None
        l=self.sortList(head); r=self.sortList(mid)
        dummy=cur=ListNode(0)
        while l and r:
            if l.val<r.val: cur.next,l=l,l.next
            else: cur.next,r=r,r.next
            cur=cur.next
        cur.next=l or r; return dummy.next
