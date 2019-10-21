class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 :
            return 1 
        
        c1 = 1
        c2 = 1
        c3 = 1
        m = 2
        
        ugly_numbers = [1,1]
        while m<=n:
            if ugly_numbers[c1]*2 < ugly_numbers[c2]*3 and ugly_numbers[c1]*2 < ugly_numbers[c3]*5:
                ugly_numbers.append(ugly_numbers[c1]*2)
                c1 = c1+1
            elif ugly_numbers[c2]*3 < ugly_numbers[c1]*2 and ugly_numbers[c2]*3 < ugly_numbers[c3]*5:
                ugly_numbers.append(ugly_numbers[c2]*3)
                c2 = c2+1
            elif ugly_numbers[c3]*5 < ugly_numbers[c2]*3 and ugly_numbers[c3]*5 < ugly_numbers[c1]*2:
                ugly_numbers.append(ugly_numbers[c3]*5)
                c3 = c3+1    
            elif ugly_numbers[c1]*2 == ugly_numbers[c2]*3 and ugly_numbers[c3]*5 == ugly_numbers[c1]*2:
                ugly_numbers.append(ugly_numbers[c1]*2)
                c1 = c1+1
                c2 = c2+1
                c3 = c3+1
            elif ugly_numbers[c1]*2 == ugly_numbers[c2]*3:
                ugly_numbers.append(ugly_numbers[c1]*2)
                c1 = c1+1
                c2 = c2+1
            elif ugly_numbers[c1]*2 == ugly_numbers[c3]*5:
                ugly_numbers.append(ugly_numbers[c1]*2)
                c1 = c1+1
                c3 = c3+1
            elif ugly_numbers[c3]*5 == ugly_numbers[c2]*3:
                ugly_numbers.append(ugly_numbers[c2]*3)
                c3 = c3+1
                c2 = c2+1                
            m = m+1        
        return ugly_numbers[m-1]
