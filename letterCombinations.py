class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        res = ['']
        for i in list(digits):
            if i in mapping:
                lis = list(mapping[i])
                res = [(jitem+item) for item in lis for jitem in res]
            else:
                return None
        return res
