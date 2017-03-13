# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Problem url.

from list_node import ListNode


class Solution(object):
  """
  >>> solution = Solution()
  """

  def rotateRight(self, head, k):

    if not head:
      return head
    if not head.next:
      return head

    n = self._listLength(head)
    k = k % n
    if k == 0:
      return head

    step = 0
    # Cut between prev and curr, where curr as new head.
    prev = head
    curr = head.next
    while curr:
      if step + k + 1 == n:  #
        break
      prev = curr
      curr = curr.next
      step += 1

    tail = curr
    while tail.next:
      tail = tail.next

    prev.next = None
    tail.next = head
    return curr

  def _listLength(self, head):
    n = 0
    while head:
      n += 1
      head = head.next
    return n


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  head = ListNode.FromList(['a', 'b', 'c'])
  s = Solution()
  head = s.rotateRight(head, 1)
  print head
