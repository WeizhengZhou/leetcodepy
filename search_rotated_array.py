# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.search([4, 5, 6, 7, 0, 1, 2], 0)
  4
  >>> solution.search([4, 5, 6, 7, 0, 1, 2], 7)
  3
  >>> solution.search([4, 5, 6, 7, 0, 1, 2], -3)
  -1
  >>> solution.search([5, 1, 3], 5)
  0
  """

  def search(self, nums, target):
    return self._search(nums, target, 0, len(nums) - 1)

  def _search(self, nums, target, left, right):
    if left > right:
      return -1
    middle = (left + right) / 2
    if nums[middle] == target:
      return middle
    elif nums[middle] < target:
      if nums[left] < nums[right]:
        return self._search(nums, target, middle + 1, right)
      else:
        left_res = self._search(nums, target, left, middle - 1)
        right_res = self._search(nums, target, middle + 1, right)
        if left_res != -1:
          return left_res
        if right_res != -1:
          return right_res
        return -1

    else:  # nums[middle] > target
      if nums[left] < nums[right]:
        return self._search(nums, target, left, middle - 1)
      else:
        left_res = self._search(nums, target, left, middle - 1)
        right_res = self._search(nums, target, middle + 1, right)
        if left_res != -1:
          return left_res
        if right_res != -1:
          return right_res
        return -1
        

if __name__ == '__main__':
  import doctest
  doctest.testmod()
