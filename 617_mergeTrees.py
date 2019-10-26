# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None 
            
        if t1 == None:
            v1 = 0
            l1 = None
            r1 = None
        else: 
            v1 = t1.val
            l1 = t1.left
            r1 = t1.right
            
        if t2 == None:
            v2 = 0
            l2 = None
            r2 = None
        else:
            v2 = t2.val
            l2 = t2.left
            r2 = t2.right
            
        t = TreeNode(v1 + v2)
        t.left = self.mergeTrees(l1,l2)
        t.right = self.mergeTrees(r1,r2)        
        return t
