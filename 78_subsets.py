import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums, []]
        
        cnums = copy.copy(nums)
        el = cnums.pop()
        
        s1 = self.subsets([el])
        s2 = self.subsets(cnums)
        
        res = []
        for item1 in s1:
            for item2 in s2:
                if item1 != [] and item2 != []:
                    res.append(item2)
                    res.append(item1+item2)
            if item1 != []:
                res.append(item1)
        res.append([])                    
        return res
