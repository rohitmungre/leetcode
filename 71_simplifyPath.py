class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == "":
            return path
        parr = path.split('/')
        varr = []
        for item in parr:
            if str(item) != '' and str(item) != '.':
                if str(item) == '..':
                    if len(varr) > 0: 
                        varr.pop()
                else:
                    varr.append(str(item))
        return '/'+'/'.join(varr)
