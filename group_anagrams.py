# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def groupAnagrams(self, strs):
    if not strs:
      return []
    group_by_key = dict() 
    for s in strs:
      sorted_s = ''.join(sorted(s))
      if group_by_key.get(sorted_s):
        group_by_key[sorted_s].append(s)
      else:
        group_by_key[sorted_s] = [s,]
    return [list(v) for v in group_by_key.values()]


if __name__ == '__main__':
  strs = ["eat", "tea", "tan", "ate", "nat", "bat", "", ""]
  s = Solution()
  print s.groupAnagrams(strs)
  # import doctest
  # doctest.testmod()
