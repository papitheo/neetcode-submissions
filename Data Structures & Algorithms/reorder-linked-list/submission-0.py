# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # point both first and slow to the head
        fast = slow = head
        # iterate through the list with first.next amd first.next.next
        while fast.next and fast.next.next:
            # pass fast.next to slow and fast.next.next to fast
            slow = slow.next
            fast = fast.next.next 
        # assign slow.next node to second and set slow.next to none (set the end of the furst half to none)
        second = slow.next
        slow.next = None
        # declare prev=None
        previous_Node = None
        # Reverse the second
        while second:
            # next_node = second.next
            next_node = second.next
            # second.next = prev
            second.next = previous_Node
            # prev = second
            previous_Node = second
            # second = next_node
            second = next_node   
        # point first = head 
        first = head 
        second = previous_Node
        # while second:
        while second:
            # save the second node of the first half
            f_nextNode = first.next
            # save the second node of the second half
            s_nextNode = second.next
            # point the head (first node) to first node of the second half 
            first.next = second
            # point the first node of the second half to the first node of the first half
            second.next = f_nextNode
            # Assign the second node of the first half to first
            first = f_nextNode
            # Assign the second node of the second half to second
            second = s_nextNode
