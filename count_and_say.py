# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.countAndSay(1)
  '1'
  >>> solution.countAndSay(2)
  '11'
  >>> solution.countAndSay(3)
  '21'
  >>> solution.countAndSay(4)
  '1211'
  >>> solution.countAndSay(5)
  '111221'
  """

  def countAndSay(self, n):
    return self._countAndSay('1', n-1)

  def _countAndSay(self, s, remaining_count):
    if remaining_count <= 0:
      return s
    curr = s[0]
    count = 1
    i = 1
    res = ''
    while i < len(s):
      if s[i] == curr:
        count += 1
      else:
        res += (str(count) + curr)
        curr = s[i]
        count = 1
      i += 1
    res += (str(count) + curr)
    return self._countAndSay(res, remaining_count - 1)


if __name__ == '__main__':
  import doctest
  doctest.testmod()

