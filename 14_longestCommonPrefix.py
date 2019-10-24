class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        pidx = 0
        pr = ''
        tmp = ''
        for pidx in range(0, len(min(strs))):
            for idx, item in enumerate(strs):
                if idx == 0:
                    tmp = item[pidx]            
                elif item[pidx]==tmp:
                    if idx == len(strs)-1: 
                        pr = pr + tmp
                else:
                    return pr            
        return pr 
                
