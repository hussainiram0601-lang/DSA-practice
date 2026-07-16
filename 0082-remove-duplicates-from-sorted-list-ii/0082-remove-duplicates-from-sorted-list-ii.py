# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that points to head
        dummy = ListNode(0, head)
        
        # 'slow' always points to the last known distinct node
        slow = dummy
        
        while slow.next and slow.next.next:
            # Check if the next two nodes have duplicate values
            if slow.next.val == slow.next.next.val:
                duplicate_val = slow.next.val
                # Keep moving past all nodes containing this duplicate value
                while slow.next and slow.next.val == duplicate_val:
                    slow.next = slow.next.next
            else:
                # No duplicates found, move the slow pointer forward
                slow = slow.next
                
        return dummy.next

        