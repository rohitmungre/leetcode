# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        pointer = head
        for i in range(m-2):
            pointer = pointer.next
        if m>1:            
            pr = pointer.next
        else:
            pr = head
        revhead = pr
        prn = pr.next
        pr.next = None
        
        for j in range(n-m):
            tmp = prn.next 
            prn.next = pr
            pr = prn
            prn = tmp
            
        revhead.next = prn
        if m > 1:
            pointer.next = pr   
        else:
            head = pr
        return head        
        
