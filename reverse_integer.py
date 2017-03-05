class Solution(object):
  """Reverse digits of an integer.
  >>> Solution().reverse(123)
  321
  >>> Solution().reverse(12345678901)
  0
  >>> Solution().reverse(-789)
  -987
  """
  MAX_INT = 2**31-1
  MIN_INT = -2**31 

  def reverse(self, x):

    if x > 0:
      return self._reversePositive(x)
    else:
      return -self._reversePositive(-x)

  def _IsOverflowed(self, x):
    return x > self.MAX_INT or x < self.MIN_INT


  def _reversePositive(self, x):
    reversed_x = 0
    while x:
      reversed_x *= 10
      reversed_x += x % 10
      x /= 10
      if self._IsOverflowed(reversed_x):
        return 0
    return reversed_x

if __name__ == '__main__':
  import doctest
  doctest.testmod()