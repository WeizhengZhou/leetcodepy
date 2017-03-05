# https://leetcode.com/problems/valid-parentheses/?tab=Description

import collections

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.isValid('([)')
  False
  >>> solution.isValid('([])')
  True
  >>> solution.isValid('[]')
  True
  """

  LEFT_BY_RIGHT = {
      ')': '(',
      ']': '[',
      '}': '{'
  }
  LEFTS = ['(', '[', '{']
  RIGHTS = [')', ']', '}']
  
  def isValid(self, s):
    if not s or len(s) % 2 == 1:
      return False
    dq = collections.deque()
    dq.append(s[0])
    for elem in s[1:]:
      if elem in self.LEFTS:
        dq.append(elem)
      else:
        left = dq[-1]
        right = elem
        if self.LEFT_BY_RIGHT[right] != left:
          return False
        else:
          dq.pop()
    if dq:
      return False
    return True


if __name__ == '__main__':
  import doctest
  doctest.testmod()
