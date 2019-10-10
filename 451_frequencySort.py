class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
        
        sorted_lis = []
        for i in range(0, len(dic)):
            maxx = 0
            max_el = ''
            for j in dic:
                if dic[j] > maxx and j not in sorted_lis:
                    maxx = dic[j]
                    max_el = j 
            sorted_lis.append(max_el)
            
        res = ''
        for i in sorted_lis:
            for j in range(0, dic[i]):
                res = res + i

        return res
