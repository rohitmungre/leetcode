import copy
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        cpeople = copy.deepcopy(people)
        return self.rq(cpeople, people)        
        
    def rq(self, people,cp):
        if len(people) == 0:
            return []
        if len(people) == 1:
            return cp
        flag = 0
        for idx, item in enumerate(people):
            if item[1] == 0:
                if flag == 0:
                    min_height = item[0]
                    min_idx = idx
                    flag = 1
                else:
                    if item[0] < min_height:
                        min_height = item[0]
                        min_idx = idx
        res = []
        min_zero = people.pop(min_idx)
        actual_min_zero = cp.pop(min_idx)

        for idx, item in enumerate(people):
            if item[0]<=min_height:
                item[1] = item[1]-1
        
        res = [actual_min_zero] + self.rq(people, cp)
        return res
