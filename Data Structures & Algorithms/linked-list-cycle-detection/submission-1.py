# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ##tort and hare pointers
        ##start both from beginning
        ## increment slow by 1 and fast by 2 nodes
        ## also you could jsut use a set
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow ==fast:
                return True
        return False