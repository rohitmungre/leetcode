class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return self.mp_dp(x,n,{})
    
    def mp_dp(self, x, n , memo):
        if n in memo:
            return memo[n]
        print(n)
        if n == 0:
            memo[n] = 1.0
            return 1.0
        if n in [-1,1]:
            if n == -1:
                xx = 1/x
            else:
                xx = x
            memo[n] = xx
            return xx
        elif n <0:
            xx = 1/self.myPow(x, abs(n))
        else:
            y = self.myPow(x, n/2)
            if abs(n)%2 == 0:                
                xx = y*y
            else:
                xx = y*y*x         
        memo[n] = xx
        return xx
