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
        if not l1:
            return l2
        if not l2:
            return l1
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while l1 and l2:
            sum_value = l1.val + l2.val + carry
            curr.next = ListNode(sum_value % 10)
            carry = sum_value / 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        remain_list = l1 or l2
        while remain_list:
            sum_value = remain_list.val + carry
            curr.next = ListNode(sum_value % 10)
            carry = sum_value / 10
            remain_list = remain_list.next
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return dummy_head.next
            
            
            
            
        