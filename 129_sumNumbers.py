# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return root.val

        res = self.sn(root)
        sum = 0
        for item in res:
            sum = sum + item[0]            
        return sum
        
    def sn(self, root):
        if root == None:
            return [[0,0]]
        
        if root.left == None and root.right == None:
            return [[root.val,1]]
            
        a1 =self.sn(root.left)
        a2 =self.sn(root.right)
        
        res = []
        if a1 != [[0,0]]:
            for aa1 in a1:
                v = int(math.pow(10, aa1[1]))*(root.val)+ aa1[0]
                h = aa1[1]+1
                res.append([v,h])
        if a2 != [[0,0]]:
            for aa2 in a2:
                v = int(math.pow(10, aa2[1]))*(root.val)+ aa2[0]
                h = aa2[1]+1
                res.append([v,h])
        return res
