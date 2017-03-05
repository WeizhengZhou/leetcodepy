class Solution(object):
  """
  >>> Solution()._getDigits(121)
  3
  >>> Solution()._getDigits(0)
  0
  >>> Solution()._getDigits(-12)
  2
  >>> Solution().isPalindrome(-2147483648)
  False
  >>> [Solution().isPalindrome(x) for x in [1, 12, 121, 12321, -2147483648]]
  [True, False, True, True, False]
  """

  def isPalindrome(self, x):
    if x == 0:
      return True

    if x < 0:
      x = -x
    return self._isPalindrome(x)
  
  def _isPalindrome(self, x):
    digits = self._getDigits(x) - 1

    while x:

      head = x / (10**digits)
      tail = x % 10
      if head != tail:
        return False
      x -= head * 10**digits
      x /= 10

      digits -= 2
    return True

  def _getDigits(self, x):
    x = abs(x)
    n = 0
    while x:
      n += 1
      x /= 10
    return n


if __name__ == '__main__':
  # Solution().isPalindrome(12321)
  import doctest
  doctest.testmod()
