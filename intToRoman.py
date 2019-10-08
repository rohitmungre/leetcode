class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        m_val = num/1000
        d_val = (num-(m_val*1000))/500
        c_val = (num-(m_val*1000)-(d_val*500))/100
        l_val = (num -(m_val*1000)-(d_val*500)-(c_val*100))/50    
        x_val = (num -(m_val*1000)-(d_val*500)-(c_val*100) - (l_val*50))/10
        v_val = (num -(m_val*1000)-(d_val*500)-(c_val*100) - (l_val*50) - (x_val*10))/5
        i_val = (num -(m_val*1000)-(d_val*500)-(c_val*100) - (l_val*50) - (x_val*10) - (v_val*5))                
              
        res = ''
        for i in range(0,m_val):
        	res = res + 'M' 
        for i in range(0,d_val):
        	res = res + 'D'
        for i in range(0,c_val):
        	res = res + 'C'
        for i in range(0,l_val):
        	res = res + 'L'
        for i in range(0,x_val):
        	res = res + 'X' 
        for i in range(0,v_val):
        	res = res + 'V'
        for i in range(0,i_val):
        	res = res + 'I'
        
        res =res.replace('VIIII', 'IX')
        res =res.replace('IIII', 'IV')
        res =res.replace('LXXXX', 'XC')
        res =res.replace('XXXX', 'XL')
        res =res.replace('DCCCC', 'CM')
        res =res.replace('CCCC', 'CD')
        
        
        return res

