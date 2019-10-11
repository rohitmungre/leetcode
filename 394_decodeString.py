class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_stack = []
        num_stack = []
        pre_stack = []
        cst_stack = []
        pre = ''
        cst = ''
        for i,c in enumerate(s):
            if c in '0123456789':
                if s[i-1] in '0123456789':
                    num = num_stack.pop()
                    num_stack.append(10*num+int(s[i]))
                else:
                    num_stack.append(int(s[i])) 
                    pre_stack.append(pre)
                    pre = ''
            elif c == '[':
                start_stack.append(i)
            elif c == ']' and start_stack: 
                start = start_stack.pop()
                num = num_stack.pop()
                prefix = pre_stack.pop()
                st = pre
                cst = ''
                for i in range(0,num):
                    cst = cst + st
                cst = prefix + cst
                cst_stack.append(cst)
                pre = cst
            else:
                pre = pre + c
                
        return pre
