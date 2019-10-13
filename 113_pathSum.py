# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        
        p1 =self.pathSum(root.left, sum-root.val)
        p2 =self.pathSum( root.right, sum-root.val)
        res = []
        if p1 != []:
            for pp1 in p1:
                res.append([root.val]+pp1)
        if p2 != []:
            for pp2 in p2:
                res.append([root.val]+pp2)

        return res
