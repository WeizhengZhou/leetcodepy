# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def permute(self, nums):
    if not nums:
      return [[],]
    if len(nums) == 1:
      return [[nums[0],],]
    rest = self.permute(nums[1:])
    solutions = []
    for r in rest:
      for i in range(len(r) + 1):
        solutions.append(r[:i] + [nums[0],] + r[i:])
    return solutions


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  s = Solution()
  print s.permute([1,2])
