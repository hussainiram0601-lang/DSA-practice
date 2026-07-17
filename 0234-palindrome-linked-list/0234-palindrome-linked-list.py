# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = 0
        curr = head
        while curr!=None:
            curr = curr.next
            l+=1
        curr = head
        for i in range(l//2):
            curr = curr.next
        prev = None
        nxt = None
        while curr!= None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left = head
        right = prev
        while right!=None:
            if right.val!= left.val:
                return False
            left = left.next
            right = right.next
        return True