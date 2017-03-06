# Problem url.

import heapq


class Solution(object):
  """
  >>> from list_node import ListNode
  >>> node_1 = ListNode.FromList([2, 5])
  >>> node_2 = ListNode.FromList([1, 3])
  >>> node_3 = ListNode.FromList([0, 7])
  >>> solution = Solution()
  >>> print solution.mergeKLists([node_1, node_2, node_3])
  0 -> 1 -> 2 -> 3 -> 5 -> 7
  """

  def mergeKLists(self, list_nodes):
    if not list_nodes:
      return None
    # Push tuple into heap, where the first element is the priority.
    heap = [(node.val, node) for node in list_nodes if node]  
    heapq.heapify(heap)

    dummy_head = ListNode(0)
    curr = dummy_head
    while heap:
      key, top = heapq.heappop(heap)  # Pop priority and element.
      curr.next = top
      curr = curr.next
      if top.next:
        heapq.heappush(heap, (top.next.val, top.next))
    return dummy_head.next


if __name__ == '__main__':
  import doctest
  doctest.testmod()
