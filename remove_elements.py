# https://leetcode.com/problems/remove-element/?tab=Description

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.removeElement([], 4)
  0
  >>> solution.removeElement([4], 1)
  1
  >>> solution.removeElement([2, 4, 1, 4], 4)
  2
  >>> solution.removeElement([2, 4, 1, 4], 1)
  3
  >>> solution.removeElement([3, 2, 2, 3], 3)
  2
  """

  def removeElement(self, nums, val):
    if not nums:
      return 0
    tail = 0
    curr = 0
    gabage = len(nums) - 1
    while curr <= gabage:
      if nums[curr] == val:
        nums[curr], nums[gabage] = nums[gabage], nums[curr]
        gabage -= 1
      else:
        nums[tail] = nums[curr]
        tail += 1
        curr += 1

    return tail


if __name__ == '__main__':
  import doctest
  doctest.testmod()
