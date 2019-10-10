class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]        
        res = self.gc_dp(n,{})       
        return res
    
    def gc_dp(self, n , memo):
        if n in memo:
            return memo
        if n == 0:
            memo[0] = [0]
            return [0]
        if n == 1:
            memo[1] = [0,1]
            return [0,1]

        prev_arr = self.grayCode(n-1)
        res = []
        for i in range(0,2):
            for j in range(0, len(prev_arr)):
                if i ==0:
                    res.append(prev_arr[j])
                else:
                    res.append(prev_arr[len(prev_arr) - j -1]+len(prev_arr))
        memo[n] = res
        return res
