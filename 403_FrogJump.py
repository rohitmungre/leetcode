import copy 
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 0:
            return False
        return self.cc_dp(stones, 0, [], {})                
                
    def cc_dp(self, stones, idx, steps, memo):        
        if idx == len(stones)-1:
            return True
        if idx == 0: 
            if stones[1] != 1:
                return False        
            k = 0
            csteps = copy.copy(steps)
            csteps.append(1)
            return self.cc_dp(stones, 1 , csteps, memo)
        else:
            k = steps[-1]
        
        mstr = str(idx) + '~' + str(k)
        if mstr in memo:
            return memo[mstr]
        
        stm1 = stones[idx] + k-1
        st0 = stones[idx] + k
        stp1 = stones[idx] + k+1
        
        if stm1 not in stones and stp1 not in stones and st0 not in stones:
            memo[mstr] = False
            return False
        
        if stp1 not in stones and st0 not in stones and k==1:
            memo[mstr] = False
            return False
        
        if stp1 in stones:
            csteps = copy.copy(steps)
            csteps.append(k+1)
            rp = self.cc_dp(stones, stones.index(stp1), csteps, memo)
            if rp:
                memo[mstr] = True
                return True
        
        if stm1 in stones and k !=1 :
            csteps = copy.copy(steps)
            csteps.append(k-1)
            rm = self.cc_dp(stones, stones.index(stm1), csteps, memo)
            if rm:
                memo[mstr] = True
                return True
        
        if st0 in stones and k !=0 :
            csteps = copy.copy(steps)
            csteps.append(k)
            r0 = self.cc_dp(stones, stones.index(st0), csteps, memo)
            if r0:
                memo[mstr] = True
                return True

        memo[mstr] = False
        return memo[mstr]
