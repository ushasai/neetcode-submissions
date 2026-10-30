# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        

        while l1 or l2:
            summ = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if summ >= 10:
                carry = summ//10
                tail.next = ListNode(summ%10)
                tail = tail.next
            else:
                carry = 0
                tail.next = ListNode(summ%10)
                tail = tail.next
            l1 = (l1.next if l1 else l1)
            l2 = (l2.next if l2 else l2)
        if carry:
            tail.next = ListNode(carry)   

        return dummy.next

        