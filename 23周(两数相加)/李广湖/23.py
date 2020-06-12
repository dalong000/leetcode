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
        temp =  0
        res = l = ListNode(0)
        while l1 or l2:
            value = temp
            if l1: 
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            
            temp = value // 10
            l.next = ListNode(value % 10)
            l = l.next
            
        if temp:
            l.next = ListNode(temp)
            
        return res.next