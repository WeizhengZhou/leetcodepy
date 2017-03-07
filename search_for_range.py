# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.searchRange([1, 3, 3, 5], 2)
  [-1, -1]
  >>> solution.searchRange([1, 3, 3, 4], 3)
  [1, 2]
  """

  def searchRange(self, nums, target):
    return self._searchRange(nums, 0, len(nums)-1, target)

  def _searchRange(self, nums, left, right, target):
    pass


if __name__ == '__main__':
  solution = Solution()
  print solution.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4)
  # import doctest
  # doctest.testmod()
