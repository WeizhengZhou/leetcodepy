# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.divide(1, 0)
  2147483647
  >>> solution.divide(0, -1)
  0
  >>> solution.divide(1, 2)
  0
  >>> solution.divide(5, 2)
  2
  >>> solution.divide(-3, 2)
  -1
  >>> solution.divide(1, 1)
  1
  >>> solution.divide(1, -1)
  -1
  """
  def divide(self, dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if divisor == 0:
      return if dividend > 0 else -2**32
    sign = self._getSign(dividend, divisor)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    res = divisor
    while res <= dividend:
      count += 1
      res += divisor
    return count if sign == 1 else -count


  def _getSign(self, dividend, divisor):
    sign = 1
    if dividend < 0 and divisor > 0:
      sign = -1
    if dividend > 0 and divisor < 0:
      sign = -1
    return sign



if __name__ == '__main__':
  import doctest
  doctest.testmod()
