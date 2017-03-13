# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# https://leetcode.com/problems/multiply-strings/?tab=Description

import collections




class Solution(object):
  """
  >>> s = Solution()
  >>> print s.add('123', '7')
  130
  >>> print s.multiply('12', '12')
  144
  """

  def multiply(self, a, b):
    result = ''
    for i in range(len(b)):
      tmp = self.add(a, b[len(b) - 1 - i])
      result += '0' * i
      result = self.add(tmp, result)
      print tmp, result
    return result




  def add(self, a, b):
    carry = 0
    dq = collections.deque()
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      dq.appendleft(str(carry % 10))
      carry /= 10
    if carry == 1:
      dq.appendleft('1')
    return ''.join([str(e) for e in dq])


if __name__ == '__main__':
  import doctest
  doctest.testmod()
