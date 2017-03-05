# https://leetcode.com/problems/4sum/?tab=Description

class Solution(object):
  """
  >>> Solution().fourSum()
  result
  """

  def fourSum(self, nums, target):
    if not nums or len(nums) < 4:
      return []
    nums.sort()

    n = len(nums)
    index_1 = 0
    index_4 = n - 1

    while index_1 <= index_4:
      two_sum_solutions = self._twoSum(
          nums[index_1 + 1 : index_4],
          target - nums[index_1] - nums[index_2]
      )
      if not two_sum_solutions:
        

  def _twoSum(self, nums, target):
    # Assume sorted.
    l = 0
    r = len(nums) - 1
    solutions = []
    while l < r:
      two_sum = nums[l] + nums[r]
      if two_sum == 0:
        solutions.append((nums[l], nums[r]))
        l = self._skipDuplicates(nums, l)
      elif two_sum <= 0:
        l += 1
      else:
        r -= 1
    return solutions

  def _skipDuplicates(self, nums, index):
    curr = index + 1:
    while curr < len(nums) and nums[curr] == nums[index]:
      curr += 1
    return curr




if __name__ == '__main__':
  import doctest
  doctest.testmod()
