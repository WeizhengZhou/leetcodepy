# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

# https://leetcode.com/problems/first-missing-positive/?tab=Description


class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.firstMissingPositive([-1, 3, 2])
  1
  >>> solution.firstMissingPositive([1, 3, 7])
  2
  >>> solution.firstMissingPositive([1, 1])
  2
  """

  def firstMissingPositive(self, nums):
    i = 0
    while i < len(nums):
      magic_index = nums[i] - 1
      if magic_index not in range(len(nums)) or nums[magic_index] == magic_index + 1:
        i += 1
        continue
      buf = nums[magic_index]
      nums[magic_index] = nums[i]
      nums[i] = buf

    for i in range(len(nums)):
      if i + 1 != nums[i]:
        return i + 1
    return len(nums) + 1


if __name__ == '__main__':
  import doctest
  doctest.testmod()
  # solution = Solution()
  # print solution.firstMissingPositive([-1, 3, 2])
