# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root ==None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        dic = {}
        dic = self.lv(root,0, dic)
        res = []
        for keys in dic:
            mx = max(dic[keys])
            res.append(mx)
        return res
        
    def lv(self, root, height, dic):
        if root == None:
            return dic
        if height in dic:
            dic[height].append(root.val)
        else:
            dic[height] = [root.val]
        if root.left != None:
            dic = self.lv(root.left, height+1, dic)
        if root.right != None:
            dic = self.lv(root.right, height+1, dic)
        return dic
        
        
