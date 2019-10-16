# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None:
            return root.val
        lot_dict = {}        
        self.lot_h(root,0,lot_dict)
        return lot_dict[max(lot_dict)][0]
        
    def lot_h(self, root, height, lot_dict):
        if root == None:
            return 
        if height in lot_dict:
            lot_dict[height].append(root.val)
        else:
            lot_dict[height] = [root.val]
        if root.left != None:
            self.lot_h(root.left, height+1, lot_dict)
        if root.right != None:
            self.lot_h(root.right, height+1, lot_dict)
