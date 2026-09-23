# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle - this will leave slow.next to be the
        # start of the next half and fast will be pointing to 
        # the end of that half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second - remember to follow the chain
        # when reversing link lists
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
