# https://leetcode.com/problems/longest-common-prefix/?tab=Description

class Solution(object):
  """
  >>> Solution().longestCommonPrefix(['a', 'ac', 'abc'])
  'a'
  >>> Solution().longestCommonPrefix(['ac', 'ac', 'acd'])
  'ac'
  >>> Solution().longestCommonPrefix(['aaaaaaaa', 'd', 'z'])
  ''
  """
  def _longestCommonPrefix(self, strs):
    min_str = min(strs)
    max_str = max(strs)
    
    for i in range(len(min_str)):
      if min_str[i] != max_str[i]:
        return i

    return min_str[:i + 1]

  def longestCommonPrefix(self, strs):
    if not strs:
      return ''
    if len(strs) == 1:
      return strs[0]
    if not strs[0]:
      return ''

    min_length = min([len(s) for s in strs])

    for i in range(min_length):
      curr_char = strs[0][i]
      for j in range(len(strs)):
        if strs[j][i] != curr_char:
          return strs[0][:i]
    return strs[0][:min_length]


if __name__ == '__main__':
  import doctest
  doctest.testmod()
