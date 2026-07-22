# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # Both nodes are None -> symmetric at this branch
            if not t1 and not t2:
                return True
            # One node is None and the other isn't -> not symmetric
            if not t1 or not t2:
                return False
            # Values must match, and outer/inner subtrees must be mirror images
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)