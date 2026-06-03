# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##create a prev equal to none
        ##have curr set to head0
        ##while curr is not null, have temp = curr.next
        ##curr.next = prev
        ##prev = curr
        ##curr = temp


   



        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        