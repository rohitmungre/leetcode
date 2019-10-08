class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        idx = 0
        sign = 1
        start_idx = -1
        end_idx = -1
        sign_flag = True
        while idx<len(str):
            if str[idx] == ' ' and start_idx == -1 and sign_flag:
                idx = idx+1
            elif str[idx] == '-' and start_idx == -1 and sign_flag:
                sign_flag = False
                sign = -1
                idx = idx+1
            elif str[idx] == '+' and start_idx == -1 and sign_flag:
                idx = idx + 1
                sign_flag = False
            elif str[idx].isdigit():
                if start_idx == -1:
                    start_idx = idx
                idx = idx+1
            else:
                break
        
        if start_idx == -1:
            return 0
        end_idx = idx 
        num = int(str[start_idx:end_idx])
        num = num*sign
        
        if num>pow(2,31)-1:
            return pow(2,31) - 1
        
        if num<-1*pow(2,31):
            return -1*pow(2,31)

        return num
