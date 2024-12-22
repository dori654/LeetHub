# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next =head
        prev = dummy

        cur = head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                while cur.next is not None and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next

            else:
                prev = cur
            cur = cur.next
                
        return dummy.next