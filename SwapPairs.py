# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        if head.next == None:
            return head
        ptr = head
        nptr = head.next  
        
        dummy = ListNode(0)
        dummy.next = head.next
        prev_ptr = None
        nnptr = nptr.next
        while ptr != None:
            ptr.next = nnptr
            nptr.next = ptr
            if prev_ptr != None:
                prev_ptr.next = nptr
                  
            prev_ptr = ptr
            ptr = nnptr
            if ptr == None:
                break
            nptr = nnptr.next
            if nptr == None:
                break
            nnptr = nptr.next
        return dummy.next
        
        
