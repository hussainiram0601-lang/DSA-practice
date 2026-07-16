# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        
        while curr!=None:
            curr = curr.next
            l+=1
        curr = head
        if l == n:
          return head.next
        for i in range(l-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
        