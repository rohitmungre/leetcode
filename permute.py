import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        res = []
        for i in range(0, len(nums)):
            cnums = copy.copy(nums)
            el = cnums.pop(i)
            m_el = self.permute(cnums)
            for j in range(0, len(m_el)):
                tmp =[el]+m_el[j]
                m_el[j]=tmp
            res=res+m_el
        return res
            
            
