class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for item in arr:
            if item in dic:
                dic[item] = dic[item]+1
            else:
                dic[item] = 1
            
        un = []
        for key in dic:
            if dic[key] in un:
                return False
            un.append(dic[key])
            
        return True
