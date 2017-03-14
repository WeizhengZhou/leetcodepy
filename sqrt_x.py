# Implement int sqrt(int x).

# Compute and return the square root of x.


# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def mySqrt(self, x):
    if x < 0:
      raise
    if x == 0:
      return 0

    return self._searchSqrt(x, 1, x)


  def _searchSqrt(self, x, l, r):
    print l, r
    m = (l + r) /2
    curr_square = m * m
    next_square = (m + 1) * (m + 1)
    if curr_square <= x:
      if next_square < x:
        return self._searchSqrt(x, m + 1, r)
      elif next_square == x:
        return m + 1
      else:
        return m
    else:
      return self._searchSqrt(x, l, m-1)


if __name__ == '__main__':
  s = Solution()
  print s.mySqrt(9)
  # for i in range(1, 10):
