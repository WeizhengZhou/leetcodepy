class ListNode(object):
  """
  >>> head = ListNode.FromList(['a', 'b', 'c'])
  >>> print str(head)
  a -> b -> c
  >>> print str(ListNode.FromList([1, 3]))
  1 -> 3
  """

  def __init__(self, x):
      self.val = x
      self.next = None

  def __str__(self):
    if not self.next:
      return str(self.val)
    return str(self.val) + ' -> ' + str(self.next)

  @classmethod
  def FromList(cls, input_list):
    if not input_list:
      return None

    head = cls(input_list[0])
    curr = head
    for value in input_list[1:]:
      curr.next = cls(value)
      curr = curr.next
    return head

if __name__ == '__main__':
  import doctest
  doctest.testmod()