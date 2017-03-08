# https://leetcode.com/problems/implement-strstr/?tab=Description

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.strStr('abcde', 'de')
  3
  >>> solution.strStr('ababc', 'abc')
  2
  >>> solution.strStr('ababc', '')
  0
  >>> solution.strStr('', 'aa')
  -1
  """
  def strStr(self, haystack, needle):
    if not needle:
      return 0

    if len(needle) > len(haystack):
      return -1
    for i in range(len(haystack)):
      if needle == haystack[i: i+len(needle)]:
       return i
    return -1



if __name__ == '__main__':
  import doctest
  doctest.testmod()
