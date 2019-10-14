# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if root == None:
            return 
        
        l = root.left
        r = root.right
        
        self.flatten(l)
        self.flatten(r)

        if l == None:
            return
        
        root.right = l
        if r != None:
            pointer = root.right
            while (pointer.right != None):
                pointer = pointer.right
            pointer.right = r
        root.left = None    
        return
