# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        pA = headA
        pB = headB
        
        flagA = False
        flagB = False
        
        while pA != pB:
            if pA.next != None:
                pA = pA.next
            else:
                flagA = True
                lastA = pA
                pA = headB                
                
            if pB.next != None:
                pB = pB.next
            else:
                flagB = True
                lastB = pB
                pB = headA

            if flagA and flagB:
                if lastA != lastB:
                    return None
                
        return pA
