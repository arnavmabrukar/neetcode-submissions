# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # No lists
        if not lists: return None

        # Keep merging until 2 lists remain
        while len(lists)>1:
            mergedLists=[]

            # Go through 2 lists at a time
            for i in range(0,len(lists),2):
                li1 = lists[i]
                li2 = lists[i+1] if (i+1)<len(lists) else None

                # Now merge and save result
                mergedLists.append(self.mergeLists(li1, li2))
            
            # Use newly merged lists for the next round
            lists = mergedLists
            
        return lists[0]

    # LC 21
    def mergeLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

        