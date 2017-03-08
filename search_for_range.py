# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.searchRange([1, 3, 3, 5], 2)
  [-1, -1]
  >>> solution.searchRange([1, 3, 3, 4], 3)
  [1, 2]
  >>> solution.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4)
  [10, 13]
  """

  def searchRange(self, nums, target):
    return [
        self._searchLeftBoundary(nums, 0, len(nums) - 1, target),
        self._searchRightBoundary(nums, 0, len(nums) - 1, target)
    ]

  def _searchLeftBoundary(self, nums, left, right, target):
    if left > right:
      return -1
    middle = (left + right) / 2
    if nums[middle] == target:
      if middle == 0:
        return middle
      elif nums[middle-1] < target:
        return middle
      else:  # nums[middle-1] == target
        return self._searchLeftBoundary(nums, left, middle-1, target)
    elif nums[middle] > target:
      return self._searchLeftBoundary(nums, left, middle - 1, target)
    else:
      return self._searchLeftBoundary(nums, middle + 1, right, target)


  def _searchRightBoundary(self, nums, left, right, target):
    if left > right:
      return -1
    middle = (left + right) / 2
    if nums[middle] == target:
      if middle == len(nums) - 1:
        return middle
      elif nums[middle + 1] > target:
        return middle
      else:  # nums[middle+1] == target
        return self._searchRightBoundary(nums, middle + 1, right, target)
    elif nums[middle] > target:
      return self._searchRightBoundary(nums, left, middle - 1, target)
    else:
      return self._searchRightBoundary(nums, middle + 1, right, target)
    

    
if __name__ == '__main__':
  # solution = Solution()
  # print solution.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4)
  import doctest
  doctest.testmod()
