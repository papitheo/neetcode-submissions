# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node (a replica of the head node)
        dummyNode = ListNode(0,head)
        # draw both fast and slow from the node 
        fast = dummyNode
        slow = dummyNode
        # move the fast node n-times
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummyNode.next


