class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        pflag = False        
        eflag = False
        sflag = False
        ssflag = False
        numflag = False
        for idx, char in enumerate(list(s)):
            if char in '0123456789':
                numflag = True
                continue
            elif char in '.':
                if pflag:
                    return False  
                else:
                    pflag = True   
                    if eflag:
                        return False  
            elif char in '-+':
                if sflag:
                    if eflag == False:
                        return False
                    elif ssflag:
                        return False
                    else:
                        ssflag = True
                        if s[idx-1] != 'e':
                            return False
                else:
                    sflag = True  
                    if idx == 0:
                        continue
                    elif s[idx-1] in '.':
                        return False
                    elif eflag == False and idx != 0:
                        return False
                    elif eflag == True and s[idx-1] != 'e':
                        return False
                if idx == len(s)-1:
                    return False
            elif char in 'e':
                if eflag:
                    return False  
                else:
                    eflag = True 
                    if idx == 0:
                        return False
                    if s[idx-1] in '-+':
                        return False
                    if idx == 1 and s[0] == '.':
                        return False
                    if idx == len(s)-1:
                        return False
            else:
                return False            
        return numflag
