# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = None
        for item in lists:
            res = self.merge2Lists(res, item)
        return res
        
    def merge2Lists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        p1 = list1
        p2 = list2
        
        if p1.val > p2.val:
            head = p2
            p2 = p2.next
        else:
            head = p1
            p1 = p1.next
        p = head  
        while p1 != None or p2 != None:
            if p1 == None:
                p.next = p2
                return head
            if p2 == None:
                p.next = p1
                return head
            if p1.val > p2.val:
                p.next = p2
                p = p2
                p2 = p2.next
            else:
                p.next = p1
                p = p1
                p1 = p1.next
                
        return head
