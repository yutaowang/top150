class Solution:
    def connect(self, root):
        cur=root
        while cur:
            dummy=Node(0); tail=dummy
            while cur:
                for child in (cur.left, cur.right):
                    if child: tail.next=child; tail=tail.next
                cur=cur.next
            cur=dummy.next
        return root
