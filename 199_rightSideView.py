# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        if root == None:
            return lis
        lis = self.rsv(root, 0, lis)        
        return lis
        
    def rsv(self, root, height, lis):
        if root == None:
            return lis
        if len(lis) < height+1:
            lis.append(root.val)
        if root.right != None:
            lis = self.rsv(root.right, height+1, lis)
        if root.left != None:
            lis = self.rsv(root.left, height+1, lis)
        return lis
