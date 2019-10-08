class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ma = 0
        
        i = 0 
        j = len(height)-1
        
        while (i<j):
            tmp_area = min(height[i], height[j])*(j-i)
            if tmp_area > ma:
                ma = tmp_area
            if height[i] == height[j]:
                i = i+1
                j = j-1
            elif height[i]> height[j]:
                j = j-1
            else:
                i = i+1
        return ma
