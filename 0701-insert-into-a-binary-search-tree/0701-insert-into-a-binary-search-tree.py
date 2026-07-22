# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if root == None:
            return newNode
        curr = root
        while curr!=None:
            if val>curr.val:
                if curr.right  == None:
                    curr.right = newNode
                    break
                else:
                    curr = curr.right
            elif val<curr.val:
                if curr.left==None:
                    curr.left = newNode
                    break
                else:
                    curr = curr.left
        return root