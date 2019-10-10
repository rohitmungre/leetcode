# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lot_dict = {}
        lot_dict = self.lot_h(root, 0, lot_dict)
        res = []
        for keys in lot_dict:
            res.append(lot_dict[keys])
        return res
    
    def lot_h(self, root, height, lot_dict):
        if root == None:
            return {}
        if height in lot_dict:
            lot_dict[height].append(root.val)
        else:
            lot_dict[height] = [root.val]
        if root.left != None:
            lot_dict = self.lot_h(root.left, height+1, lot_dict)
        if root.right != None:
            lot_dict = self.lot_h(root.right, height+1, lot_dict)
        return lot_dict
        
