# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.searchInsert([1, 3, 5, 6, 7], 0)
  0
  >>> #solution.searchInsert([1, 3, 5, 6], 2)
  1
  >>> #solution.searchInsert([1, 3, 5, 6], 3)
  1
  >>> #solution.searchInsert([1, 3, 5, 6], 4)
  2
  >>> #solution.searchInsert([1, 3, 5, 6], 7)
  4
  """

  def searchInsert(self, nums, target):
    return self._searchInsert(nums, target, 0, len(nums) - 1)

  def _searchInsert(self, nums, target, left, right):
    if left > right:
      if target < nums[right]:
        return right - 1
      elif target < nums[left]:
        return left - 1
      else:
        return left

    middle = (left + right) / 2
    if nums[middle] == target:
      return middle
    elif target < nums[middle]:
      res = self._checkInsertLeft(nums, target, middle)
      if res == -1:
        return self._searchInsert(nums, target, left, middle -1)
      else:
        return res
    else:
      res = self._checkInsertRight(nums, target, middle)
      if res == -1:
        return self._searchInsert(nums, target, middle + 1, right)
      else:
        return res

  def _checkInsertLeft(self, nums, target, middle):
    if middle == 0:
      return middle
    elif nums[middle - 1] < target:
      return middle 
    else:
      return -1

  def _checkInsertRight(self, nums, target, middle):
    if middle == len(nums) - 1:
      return middle + 1
    elif nums[middle + 1] > target:
      return middle + 1
    else:
      return -1


if __name__ == '__main__':
  import doctest
  doctest.testmod()
