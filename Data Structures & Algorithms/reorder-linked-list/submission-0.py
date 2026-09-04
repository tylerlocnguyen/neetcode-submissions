# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4 5 7 8
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        #reverse second half
    
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first = head
        second = prev
        #merge halves
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2