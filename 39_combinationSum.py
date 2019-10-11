import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) <1:
            return [[]]
        if len(candidates) == 1:
            if target%candidates[0] != 0:
                return []
        res = self.cs_dp(candidates,target, {})
        if res == [[]]:
            res = []
        return res
        
    def cs_dp(self,c,t, memo):
        mstr = '~'.join(str(cc) for cc in c) + '~' + str(t)
        if mstr in memo:
            return memo[mstr]
        if t ==0:
            memo[mstr] = []
            return []
        if len(c)<1:
            return [[]]
        cc = copy.copy(c)
        el = cc.pop(0)
        count = 0
        mar = []
        res = []
        while t - count*el >= 0:
            tmp  = self.cs_dp(cc, t-count*el,memo)
            if tmp == []:
                if mar != []:
                    res.append(tmp+mar)
            elif tmp != [[]]:
                for ii in tmp:
                    res.append(mar+ii)
            mar.append(el)
            count = count+1
        if res == []:
            res = [[]]
        memo[mstr] = res
        return res
