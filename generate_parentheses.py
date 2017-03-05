# https://leetcode.com/problems/generate-parentheses/?tab=Description

class Solution(object):
  """
  >>> Solution().methodX()
  result
  """

  def generateParenthesis(self, n):
    return self._gen('', n, n)

  def _gen(self, prefix, left, right):
    if right < left:
      return []  # No valid solutions.
    if left == 0 and right == 0:
      return [prefix,]  # Found one solution.
    # Branch current choice, and append all valid solutions.
    res = []
    if left > 0:
      res.extend(self._gen(prefix + '(', left - 1, right))
    if right > 0:
      res.extend(self._gen(prefix + ')', left, right - 1))
    return res



if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
