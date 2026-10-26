# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        curr = dummy
        for i in range(l):
            if i == l - n:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

            