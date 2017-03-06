# https://leetcode.com/problems/swap-nodes-in-pairs/?tab=Description

from list_node import ListNode


class Solution(object):
  """
  >>> solution = Solution()
  >>> print solution.swapPairs(ListNode.FromList([1, 2]))
  2 -> 1
  >>> print solution.swapPairs(ListNode.FromList([1, 2, 3]))
  2 -> 1 -> 3
  """

  def swapPairs(self, head):
    if not head or not head.next:
      return head

    dummy_head = ListNode(0)
    dummy_head.next = head
    
    p0 = dummy_head
    p1 = head
    p2 = head.next

    next_head = p2.next
    p0.next = p2
    p2.next = p1

    p1.next = self.swapPairs(next_head)
    return dummy_head.next


if __name__ == '__main__':
  import doctest
  doctest.testmod()
