# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy_root = ListNode(0)
        ptr = dummy_root
        dummy_flag = True
        while True:
            if l1 == None and l2 == None and carry == 0:
                ptr = dummy_root
                ptr = ptr.next
                return ptr
            
            if l1 != None: 
                val1 = l1.val
                l1 = l1.next
            else: 
                val1 = 0
            if l2 != None:
                val2 = l2.val
                l2 = l2.next
            else: 
                val2 = 0


            val = val1 + val2 + carry
            if val > 9:
                carry = 1
                val = val-10
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            
                                    
        ptr = dummy_root
        ptr = ptr.next
        return ptr

