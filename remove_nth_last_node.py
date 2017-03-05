# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?tab=Description


class Solution(object):
  """
  >>> from list_node import ListNode
  >>> solution = Solution()
  >>> print solution.removeNthFromEnd(ListNode.FromList('abc'), 1)
  a -> b
  >>> print solution.removeNthFromEnd(ListNode.FromList('abc'), 2)
  a -> c
  >>> print solution.removeNthFromEnd(ListNode.FromList('abc'), 3)
  b -> c
  """

  def removeNthFromEnd(self, head, n):
    if not head:
      return head
    if not head.next:
      return None

    back_index = self._removeNthFromEnd(head, n)
    if back_index == n:
      return head.next
    else:
      return head

  def _removeNthFromEnd(self, curr, target_index):
    if not curr.next:
      return 1
    back_index = self._removeNthFromEnd(curr.next, target_index)
    if back_index == target_index:
      curr.next = curr.next.next
    return back_index + 1


if __name__ == '__main__':
  # Definition for singly-linked list.
  import doctest
  doctest.testmod()
