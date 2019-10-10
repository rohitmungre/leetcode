# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        if root == None:
            return []
        lis = self.pot(root,lis)        
        return lis
        
        
    def pot(self,root,lis):
        if root == None:
            return lis
        lis.append(root.val)
        if root.left != None:
            lis = self.pot(root.left,lis)
        if root.right != None:
            lis = self.pot(root.right,lis)
        return lis        
