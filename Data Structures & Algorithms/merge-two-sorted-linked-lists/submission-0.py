# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_ptr = ListNode()
        tail_ptr = dummy_ptr


        while list1 and list2:
            if list1.val <= list2.val:
                tail_ptr.next = list1
                list1 = list1.next
            else:
                tail_ptr.next = list2
                list2 = list2.next

            tail_ptr = tail_ptr.next

        tail_ptr.next = list1 if list1 else list2
        return dummy_ptr.next
        