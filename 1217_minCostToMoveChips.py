class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """            
        d = collections.Counter([c % 2 for c in chips])
        return min(d[0], d[1])
