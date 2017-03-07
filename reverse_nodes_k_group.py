# Problem url.

from list_node import ListNode


class Solution(object):
  """
  >>> solution = Solution()
  >>> print solution.partitionList(ListNode.FromList([1, 2, 3, 4, 5]), 2)
  2 -> 1
  """

  def partitionList(self, head, n):
    partitions = []
    index = 0
    curr = head
    while curr:
      index += 1
      if index == n:
        next_head = curr.next
        curr.next = None
        partitions.append(head)
        head = next_head
        curr = head
        index = 0
      else:
        curr = curr.next
    if head:
      partitions.append(head)
    return partitions

  def reverseList(self, head):
    if not head:
      return head
    if not head.next:
      return head
    tail = head
    curr = head.next
    head = tail
    tail.next = None
    while curr.next:
      next = curr.next
      curr.next = head
      head = curr
      curr = next
    return curr


if __name__ == '__main__':
  solution = Solution()
  partitions = solution.partitionList(ListNode.FromList([1, 2, 3, 4, 5]), 2)
  print partitions[0]
  print partitions[1]
  print partitions[2]
  print solution.reverseList(ListNode.FromList([1, 2, 3, 4, 5]))
  # import doctest
  # doctest.testmod()
