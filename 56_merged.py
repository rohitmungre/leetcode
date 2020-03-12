class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) <2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged = []        
        for item in intervals:
            m_flag = True
            for mitem in merged:
                if item[0]<=mitem[1]:
                    mitem[1] = max(item[1], mitem[1])
                    m_flag = False
            if m_flag:
                    merged.append(item)
                    
        return merged
        
