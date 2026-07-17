class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        
        # They will eventually meet either at the intersection node 
        # or both become None at the same time (no intersection)
        while p1 != p2:
            # If p1 reaches the end, redirect it to headB, else move it forward
            p1 = headB if p1 is None else p1.next
            
            # If p2 reaches the end, redirect it to headA, else move it forward
            p2 = headA if p2 is None else p2.next
            
        return p1
            
        