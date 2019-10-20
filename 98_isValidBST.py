# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        r, mi, ma = self.isvalid(root)
        return r
    
    def isvalid(self, root):        
        max1 = root.val
        min2 = root.val
        min1 = root.val
        max2 = root.val
        if root.left != None:
            r1, min1, max1 = self.isvalid(root.left)
            if r1 == False or root.val <= max1:
                return False, min1, max1
            
        if root.right != None:
            r2, min2, max2 = self.isvalid(root.right)
            if r2 == False or root.val >= min2:
                return False, min2, max2
        return True, min1, max2
        
