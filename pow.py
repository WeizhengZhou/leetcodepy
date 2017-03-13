# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def myPow(self, x, n):
    if n == 0:
      return 1
    sign = -1 if n < 0 else 1
    n = abs(n)

    binary_n = self._getBinary(n)
    powers = [0] * len(binary_n)
    powers[0] = x

    for i in range(1, len(powers)):
      powers[i] = powers[i-1] * powers[i-1]

    res = 1

    for i in range(len(binary_n)):
      if binary_n[i]:
        res *= powers[i]
    if sign == 1:
      return res
    else:
      return 1. / res


  def _getBinary(self, n):
    assert n > 0
    i = 1
    binary = []
    while i <= n:
      if i & n:
        binary.append(1)
      else:
        binary.append(0)
      i <<= 1
    return binary


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  s = Solution()

  print s.myPow(3, 4)
