class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        idx = 0
        start = []
        end = []
        
        for i in timeSeries:
            if start == []:
                start.append(i)
                end.append(i+duration)
            else:
                if i>end[-1]:
                    start.append(i)
                    end.append(i+duration)
                else:
                    el = end.pop()
                    end.append(i+duration)
        count = 0
        while start != []:
            s = start.pop()
            e = end.pop()            
            count = count + (e-s)
            
        return count
